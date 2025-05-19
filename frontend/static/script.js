document.addEventListener('DOMContentLoaded', () => {
    // Get DOM elements with null checks
    const symptomInput = document.getElementById('symptomInput');
    const addSymptomBtn = document.getElementById('addSymptomBtn');
    const symptomsList = document.getElementById('symptomsList');
    const predictBtn = document.getElementById('predictBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const results = document.getElementById('results');
    const topPrediction = document.getElementById('topPrediction');
    const otherPredictions = document.getElementById('otherPredictions');
    const suggestedSymptoms = document.getElementById('suggestedSymptoms');
    const precautions = document.getElementById('precautions');
    const medicineRecommendations = document.getElementById('medicineRecommendations');
    const dietRecommendations = document.getElementById('dietRecommendations');
    const recommendedExercises = document.getElementById('recommendedExercises');
    const lifestyleRecommendations = document.getElementById('lifestyleRecommendations');
    const warningSection = document.getElementById('warningSection');
    const warningText = document.getElementById('warningText');
    const form = document.getElementById('prediction-form');

    // Set to store symptoms
    window.symptoms = new Set();

    // Add symptom when clicking the Add button
    if (addSymptomBtn) {
        addSymptomBtn.addEventListener('click', () => {
            addSymptom();
        });
    }

    // Add symptom when pressing Enter
    if (symptomInput) {
        symptomInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                addSymptom();
            }
        });
    }

    // Function to add symptoms
    function addSymptom(symptom) {
        console.log('addSymptom called with:', symptom);
        
        if (!symptom && symptomInput) {
            symptom = symptomInput.value.trim();
        } else if (!symptom) {
            return; // No input element and no symptom provided
        }
        
        // Split by comma if user pasted a list
        const symptomList = symptom.split(',');
        
        // Keep track of if we added anything
        let addedAny = false;
        
        symptomList.forEach(s => {
            const plainSymptom = s.trim().replace(/_/g, ' ');
            if (plainSymptom && !window.symptoms.has(plainSymptom)) {
                window.symptoms.add(plainSymptom);
                addedAny = true;
                console.log('Added symptom:', plainSymptom); // Debug
                console.log('Updated symptoms set:', Array.from(window.symptoms)); // Debug
            }
        });
        
        // Only update the list if we actually added anything
        if (addedAny) {
            updateSymptomsList();
        }
        
        if (symptomInput) {
            symptomInput.value = '';
            symptomInput.focus();
        }
    }

    // Make the function globally available
    window.addSymptom = addSymptom;

    // Function to remove symptoms
    function removeSymptom(symptom) {
        console.log('Removing symptom:', symptom);
        window.symptoms.delete(symptom);
        updateSymptomsList();
    }

    // Make the function globally available
    window.removeSymptom = removeSymptom;

    // Update the symptoms list in the UI
    function updateSymptomsList() {
        if (!symptomsList) return;
        
        console.log('Updating symptoms list with:', Array.from(window.symptoms)); // Debug
        
        symptomsList.innerHTML = '';
        window.symptoms.forEach(symptom => {
            const tag = document.createElement('div');
            tag.className = 'symptom-tag';
            tag.innerHTML = `
                <span>${symptom}</span>
                <button class="ml-2">
                    <i class="fas fa-times"></i>
                </button>
            `;
            
            // Add click handler properly
            const removeButton = tag.querySelector('button');
            removeButton.onclick = function() {
                window.removeSymptom(symptom);
            };
            
            symptomsList.appendChild(tag);
        });
    }

    // Function to get selected symptoms
    function getSelectedSymptoms() {
        console.log('getSelectedSymptoms called, symptoms:', window.symptoms);
        if (window.symptoms instanceof Set && window.symptoms.size > 0) {
            return Array.from(window.symptoms);
        }
        
        // Fallback to get symptoms from DOM (for legacy compatibility)
        const symptomsContainer = document.getElementById('symptomsList');
        if (symptomsContainer) {
            const symptomElements = symptomsContainer.querySelectorAll('.symptom-tag span');
            return Array.from(symptomElements).map(el => el.textContent.trim());
        }
        
        return [];
    }

    // Make the function globally available
    window.getSelectedSymptoms = getSelectedSymptoms;

    // Handle prediction button click
    if (predictBtn) {
        predictBtn.addEventListener('click', async (e) => {
            if (e) e.preventDefault();
            
            // Debug logging
            console.log('Predict button clicked');
            const currentSymptoms = getSelectedSymptoms();
            console.log('Current symptoms:', currentSymptoms);
            console.log('Symptoms count:', currentSymptoms.length);
            
            // Check if symptoms are added
            if (currentSymptoms.length === 0) {
                // Show a better error message that's more visible
                const resultsDiv = document.getElementById('results');
                if (resultsDiv) {
                    resultsDiv.innerHTML = `
                        <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-4 rounded">
                            <div class="flex items-center">
                                <div class="flex-shrink-0">
                                    <i class="fas fa-exclamation-circle text-red-500 text-xl mr-2"></i>
                                </div>
                                <div>
                                    <p class="font-bold">Please enter at least one symptom</p>
                                    <p>Use the input field above to add your symptoms.</p>
                                </div>
                            </div>
                        </div>
                    `;
                    resultsDiv.classList.remove('opacity-0');
                    resultsDiv.scrollIntoView({ behavior: 'smooth' });
                } else {
                    // Fallback to alert if results div isn't available
                    alert('Please add at least one symptom');
                }
                return;
            }

            if (loadingIndicator) loadingIndicator.classList.remove('hidden');
            if (predictBtn) predictBtn.disabled = true;
            if (results) results.style.opacity = '0';

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        symptoms: currentSymptoms
                    })
                });

                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.error || data.details || 'Unknown error occurred');
                }

                console.log('Prediction response:', data);

                // Show the results section
                if (results) {
                    results.style.opacity = '1';
                }

                // Display top prediction
                if (data.predictions && data.predictions.length > 0) {
                    const topPred = data.predictions[0];
                    console.log('Top prediction:', topPred); // Debug log

                    if (topPrediction) {
                        topPrediction.innerHTML = `
                            <h3 class="text-2xl font-bold text-gray-800 mb-2">Most Likely Disease</h3>
                            <p class="text-4xl font-bold text-blue-600 mb-2">${topPred.disease}</p>
                            <p class="text-gray-600">Confidence: ${(topPred.confidence * 100).toFixed(2)}%</p>
                            ${topPred.danger_level ? `
                                <div class="mt-2 ${topPred.danger_level === 'HIGH' ? 'text-red-600' : 'text-yellow-600'}">
                                    <i class="fas fa-exclamation-triangle mr-1"></i>
                                    Danger Level: ${topPred.danger_level}
                                </div>
                            ` : ''}
                        `;
                    }

                    // Display other predictions
                    if (otherPredictions && data.predictions.length > 1) {
                        otherPredictions.innerHTML = `
                            <h3 class="text-xl font-semibold text-gray-800 mb-4">Other Possible Diseases</h3>
                            <div class="space-y-3">
                                ${data.predictions.slice(1).map(pred => `
                                    <div class="bg-white p-4 rounded-lg shadow-sm mb-2 ${pred.confidence < 0.3 ? 'border-l-4 border-yellow-400' : ''}">
                                        <div class="flex justify-between items-center">
                                            <p class="font-semibold text-gray-800">${pred.disease}</p>
                                            <p class="text-gray-600">Confidence: ${(pred.confidence * 100).toFixed(2)}%</p>
                                        </div>
                                        ${pred.confidence < 0.3 ? `
                                            <p class="text-sm text-yellow-600 mt-2">
                                                <i class="fas fa-exclamation-triangle mr-1"></i>
                                                Low probability prediction - consider consulting a healthcare provider
                                            </p>
                                        ` : ''}
                                    </div>
                                `).join('')}
                            </div>
                        `;
                    }

                    // Display precautions if available
                    if (precautions && topPred.precautions && topPred.precautions.length > 0) {
                        precautions.innerHTML = `
                            <h3 class="text-xl font-semibold text-gray-800 mb-4">Recommended Precautions</h3>
                            <ul class="space-y-2">
                                ${topPred.precautions.map(precaution => `
                                    <li class="flex items-start space-x-2">
                                        <i class="fas fa-check-circle text-green-500 mt-1"></i>
                                        <span>${precaution}</span>
                                    </li>
                                `).join('')}
                            </ul>
                        `;
                    }

                    // Display medicine recommendations if available
                    if (medicineRecommendations && topPred.medicines && topPred.medicines.length > 0) {
                        medicineRecommendations.innerHTML = `
                            <h3 class="text-xl font-semibold text-gray-800 mb-4">Recommended Medicines</h3>
                            <div class="grid gap-4">
                                ${topPred.medicines.map(med => `
                                    <div class="border-l-4 border-blue-500 pl-4 py-2">
                                        <p class="font-semibold text-gray-800">${med.name}</p>
                                        <p class="text-gray-600 text-sm">Dosage: ${med.dosage}</p>
                                        <p class="text-gray-600 text-sm">Purpose: ${med.purpose}</p>
                                    </div>
                                `).join('')}
                            </div>
                            <p class="text-sm text-gray-500 mt-4">
                                <i class="fas fa-info-circle mr-1"></i>
                                Please consult with a healthcare professional before taking any medication.
                            </p>
                        `;
                    }

                    // Display diet recommendations if available
                    if (dietRecommendations && topPred.diet && topPred.diet.length > 0) {
                        dietRecommendations.innerHTML = `
                            <h3 class="text-xl font-semibold text-gray-800 mb-4">Recommended Diet</h3>
                            <ul class="space-y-2">
                                ${topPred.diet.map(item => `
                                    <li class="flex items-start space-x-2">
                                        <i class="fas fa-utensils text-green-500 mt-1"></i>
                                        <span>${item}</span>
                                    </li>
                                `).join('')}
                            </ul>
                        `;
                    }

                    // Display exercise recommendations if available
                    let exerciseList = topPred.exercise || topPred.exercises;
                    if (recommendedExercises && exerciseList && exerciseList.length > 0) {
                        recommendedExercises.innerHTML = `
                            <h3 class="text-xl font-semibold text-gray-800 mb-4">Recommended Exercises</h3>
                            <ul class="space-y-2">
                                ${exerciseList.map(exercise => `
                                    <li class="flex items-start space-x-2">
                                        <i class="fas fa-running text-green-500 mt-1"></i>
                                        <span>${exercise}</span>
                                    </li>
                                `).join('')}
                            </ul>
                        `;
                        recommendedExercises.classList.remove('hidden');
                    }

                    // Display lifestyle recommendations if available
                    if (lifestyleRecommendations && topPred.lifestyle && topPred.lifestyle.length > 0) {
                        console.log('Lifestyle recommendations:', topPred.lifestyle); // Debug log
                        lifestyleRecommendations.innerHTML = `
                            <h3 class="text-xl font-semibold text-gray-800 mb-4">Lifestyle Recommendations</h3>
                            <ul class="space-y-2">
                                ${topPred.lifestyle.map(item => `
                                    <li class="flex items-start space-x-2">
                                        <i class="fas fa-heart text-green-500 mt-1"></i>
                                        <span>${item}</span>
                                    </li>
                                `).join('')}
                            </ul>
                        `;
                    }

                    // Display warning if it's a critical condition
                    if (warningSection && data.critical_warning) {
                        warningSection.classList.remove('hidden');
                        warningText.innerHTML = `
                            <strong>Critical Condition Warning:</strong> 
                            The symptoms you've described may indicate a serious condition. 
                            Please seek immediate medical attention.
                        `;
                    } else if (warningSection) {
                        warningSection.classList.add('hidden');
                    }
                } else {
                    // No predictions available
                    if (topPrediction) {
                        topPrediction.innerHTML = `
                            <div class="text-center py-8">
                                <i class="fas fa-exclamation-circle text-yellow-500 text-5xl mb-4"></i>
                                <h3 class="text-2xl font-bold text-gray-800 mb-2">No Predictions Available</h3>
                                <p class="text-gray-600">Please try with different symptoms or add more symptoms for a better prediction.</p>
                            </div>
                        `;
                    }
                    if (otherPredictions) otherPredictions.innerHTML = '';
                }

                // Display suggested symptoms if available
                if (suggestedSymptoms && data.suggested_symptoms && data.suggested_symptoms.length > 0) {
                    suggestedSymptoms.innerHTML = `
                        <h3 class="text-xl font-semibold text-gray-800 mb-4">Do you also have any of these symptoms?</h3>
                        <div class="flex flex-wrap gap-2">
                            ${data.suggested_symptoms.map(symptom => `
                                <button onclick="addSymptom('${symptom}')" 
                                        class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full hover:bg-blue-200 transition-colors cursor-pointer">
                                    ${symptom.replace(/_/g, ' ')}
                                </button>
                            `).join('')}
                        </div>
                    `;
                }

            } catch (error) {
                console.error('Prediction error:', error);
                if (topPrediction) {
                    topPrediction.innerHTML = `
                        <div class="text-center py-8">
                            <i class="fas fa-exclamation-triangle text-red-500 text-5xl mb-4"></i>
                            <h3 class="text-2xl font-bold text-gray-800 mb-2">Error</h3>
                            <p class="text-gray-600">${error.message || 'An unexpected error occurred. Please try again.'}</p>
                        </div>
                    `;
                }
                if (otherPredictions) otherPredictions.innerHTML = '';
                if (suggestedSymptoms) suggestedSymptoms.innerHTML = '';
            } finally {
                if (loadingIndicator) loadingIndicator.classList.add('hidden');
                if (predictBtn) predictBtn.disabled = false;
                if (results) results.style.opacity = '1';
            }
        });
    }

    // Add form handler if form exists
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            // Use the same handler as the predict button
            if (predictBtn) {
                predictBtn.click();
            }
        });
    }

    // Add some common symptom suggestions to help users
    function addSuggestedSymptoms() {
        const commonSymptoms = [
            'fever', 'cough', 'headache', 'body pain', 
            'sore throat', 'fatigue', 'nausea', 'runny nose'
        ];
        
        const suggestionsContainer = document.createElement('div');
        suggestionsContainer.className = 'mt-4 mb-2';
        suggestionsContainer.innerHTML = `
            <p class="text-sm text-gray-600 mb-2">Common symptoms:</p>
            <div class="flex flex-wrap gap-2">
                ${commonSymptoms.map(symptom => `
                    <button type="button" 
                            onclick="addSymptom('${symptom}')" 
                            class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full hover:bg-blue-200 transition-colors cursor-pointer text-sm">
                        ${symptom}
                    </button>
                `).join('')}
            </div>
        `;
        
        const inputContainer = document.querySelector('.flex.flex-col.space-y-4.w-full');
        if (inputContainer) {
            inputContainer.appendChild(suggestionsContainer);
        }
    }

    // Add suggested symptoms
    addSuggestedSymptoms();
    
    // Add a better placeholder
    if (symptomInput) {
        symptomInput.placeholder = "Type symptoms like 'fever', 'cough', 'headache'...";
    }
});

// Emergency Support Functionality
document.addEventListener('DOMContentLoaded', function() {
    const sosButton = document.getElementById('sos-button');
    const emergencyModal = document.getElementById('emergency-modal');
    const emergencyModalContent = document.getElementById('emergency-modal-content');
    const closeEmergencyModal = document.getElementById('close-emergency-modal');
    const callAmbulanceButton = document.getElementById('call-ambulance');
    const emergencyContactsButton = document.getElementById('emergency-contacts');

    // Emergency contact numbers
    const emergencyNumbers = {
        ambulance: '102',
        police: '100',
        fire: '101',
        general: '112'
    };

    // Only add event listeners if elements exist
    if (sosButton && emergencyModal && emergencyModalContent) {
        // Toggle emergency modal with animation
        sosButton.addEventListener('click', () => {
            emergencyModal.classList.remove('hidden');
            // Trigger reflow
            emergencyModalContent.offsetHeight;
            // Add animation classes
            emergencyModalContent.classList.remove('scale-95', 'opacity-0');
            emergencyModalContent.classList.add('scale-100', 'opacity-100');
        });

        // Close emergency modal with animation
        function closeModal() {
            emergencyModalContent.classList.remove('scale-100', 'opacity-100');
            emergencyModalContent.classList.add('scale-95', 'opacity-0');
            setTimeout(() => {
                emergencyModal.classList.add('hidden');
            }, 300); // Match the duration in the CSS transition
        }

        if (closeEmergencyModal) {
            closeEmergencyModal.addEventListener('click', closeModal);
        }

        // Close modal when clicking outside
        emergencyModal.addEventListener('click', (e) => {
            if (e.target === emergencyModal) {
                closeModal();
            }
        });
    }

    // Call ambulance function with enhanced animation
    if (callAmbulanceButton) {
        callAmbulanceButton.addEventListener('click', () => {
            // Create a clickable phone link
            const phoneLink = document.createElement('a');
            phoneLink.href = `tel:${emergencyNumbers.ambulance}`;
            phoneLink.click();
            
            // Show calling status with animation
            callAmbulanceButton.classList.add('animate-pulse');
            callAmbulanceButton.innerHTML = `
                <i class="fas fa-phone text-3xl mb-2 animate-bounce"></i>
                <span class="font-semibold">Calling...</span>
                <span class="text-xs mt-1 text-red-100">${emergencyNumbers.ambulance}</span>
            `;
            
            // Reset button after 3 seconds
            setTimeout(() => {
                callAmbulanceButton.classList.remove('animate-pulse');
                callAmbulanceButton.innerHTML = `
                    <i class="fas fa-ambulance text-3xl mb-2"></i>
                    <span class="font-semibold">Call Ambulance</span>
                    <span class="text-xs mt-1 text-red-100">${emergencyNumbers.ambulance}</span>
                `;
            }, 3000);
        });
    }

    // Show emergency contacts with enhanced UI
    if (emergencyContactsButton) {
        emergencyContactsButton.addEventListener('click', () => {
            const contactsList = document.createElement('div');
            contactsList.className = 'fixed inset-0 bg-black bg-opacity-50 backdrop-blur-sm z-50 flex items-center justify-center';
            contactsList.innerHTML = `
                <div class="bg-white rounded-2xl p-6 max-w-sm w-full mx-4 shadow-2xl transform transition-all duration-300 scale-95 opacity-0">
                    <div class="flex justify-between items-center mb-6">
                        <div class="flex items-center space-x-3">
                            <i class="fas fa-phone-alt text-blue-600 text-2xl"></i>
                            <h3 class="text-xl font-bold bg-gradient-to-r from-blue-600 to-blue-500 bg-clip-text text-transparent">Emergency Contacts</h3>
                        </div>
                        <button class="text-gray-500 hover:text-gray-700 transition-colors" onclick="this.parentElement.parentElement.parentElement.remove()">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    <div class="space-y-4">
                        <a href="tel:${emergencyNumbers.ambulance}" class="flex items-center justify-between p-4 bg-gradient-to-r from-red-50 to-red-100 rounded-xl hover:from-red-100 hover:to-red-200 transform hover:scale-105 transition-all">
                            <span class="flex items-center">
                                <i class="fas fa-ambulance text-red-600 text-2xl mr-3"></i>
                                <div>
                                    <span class="font-semibold text-gray-800 block">Ambulance</span>
                                    <span class="text-sm text-gray-500">Medical Emergency</span>
                                </div>
                            </span>
                            <span class="font-bold text-red-600">${emergencyNumbers.ambulance}</span>
                        </a>
                        <a href="tel:${emergencyNumbers.police}" class="flex items-center justify-between p-4 bg-gradient-to-r from-blue-50 to-blue-100 rounded-xl hover:from-blue-100 hover:to-blue-200 transform hover:scale-105 transition-all">
                            <span class="flex items-center">
                                <i class="fas fa-shield-alt text-blue-600 text-2xl mr-3"></i>
                                <div>
                                    <span class="font-semibold text-gray-800 block">Police</span>
                                    <span class="text-sm text-gray-500">Law Enforcement</span>
                                </div>
                            </span>
                            <span class="font-bold text-blue-600">${emergencyNumbers.police}</span>
                        </a>
                        <a href="tel:${emergencyNumbers.fire}" class="flex items-center justify-between p-4 bg-gradient-to-r from-orange-50 to-orange-100 rounded-xl hover:from-orange-100 hover:to-orange-200 transform hover:scale-105 transition-all">
                            <span class="flex items-center">
                                <i class="fas fa-fire text-orange-600 text-2xl mr-3"></i>
                                <div>
                                    <span class="font-semibold text-gray-800 block">Fire Brigade</span>
                                    <span class="text-sm text-gray-500">Fire Emergency</span>
                                </div>
                            </span>
                            <span class="font-bold text-orange-600">${emergencyNumbers.fire}</span>
                        </a>
                        <a href="tel:${emergencyNumbers.general}" class="flex items-center justify-between p-4 bg-gradient-to-r from-green-50 to-green-100 rounded-xl hover:from-green-100 hover:to-green-200 transform hover:scale-105 transition-all">
                            <span class="flex items-center">
                                <i class="fas fa-phone-alt text-green-600 text-2xl mr-3"></i>
                                <div>
                                    <span class="font-semibold text-gray-800 block">General Emergency</span>
                                    <span class="text-sm text-gray-500">All Emergency Services</span>
                                </div>
                            </span>
                            <span class="font-bold text-green-600">${emergencyNumbers.general}</span>
                        </a>
                    </div>
                </div>
            `;
            document.body.appendChild(contactsList);

            // Trigger animation after append
            requestAnimationFrame(() => {
                const modalContent = contactsList.querySelector('div');
                modalContent.classList.remove('scale-95', 'opacity-0');
                modalContent.classList.add('scale-100', 'opacity-100');
            });

            // Close contacts list when clicking outside
            contactsList.addEventListener('click', (e) => {
                if (e.target === contactsList) {
                    const modalContent = contactsList.querySelector('div');
                    modalContent.classList.remove('scale-100', 'opacity-100');
                    modalContent.classList.add('scale-95', 'opacity-0');
                    setTimeout(() => {
                        contactsList.remove();
                    }, 300);
                }
            });
        });
    }
});