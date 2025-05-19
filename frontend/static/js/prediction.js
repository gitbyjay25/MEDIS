function displayRecommendations(recommendations) {
    if (!recommendations) return;

    // Display Medicine Recommendations
    const medicineRecsDiv = document.getElementById('medicineRecommendations');
    if (recommendations.medicines && recommendations.medicines.length > 0) {
        let medicineHtml = '<div class="space-y-4">';
        recommendations.medicines.forEach(med => {
            medicineHtml += `
                <div class="bg-white p-4 rounded-lg shadow">
                    <h4 class="font-semibold text-gray-800">${med.medicine}</h4>
                    <div class="mt-2 space-y-2 text-sm">
                        <p class="text-gray-600"><span class="font-medium">Dosage:</span> ${med.dosage}</p>
                        <p class="text-gray-600"><span class="font-medium">Purpose:</span> ${med.purpose}</p>
                    </div>
                </div>
            `;
        });

        // Display precautions if available
        if (recommendations.precautions && recommendations.precautions.length > 0) {
            medicineHtml += `
                <div class="mt-4 bg-blue-50 p-4 rounded-lg border border-blue-200">
                    <h4 class="font-semibold text-blue-800">Precautions:</h4>
                    <ul class="list-disc list-inside text-sm text-blue-700 mt-2">
                        ${recommendations.precautions.map(precaution => `
                            <li>${precaution.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</li>
                        `).join('')}
                    </ul>
                </div>
            `;
        }

        // Display warnings if any
        if (recommendations.warnings && recommendations.warnings.length > 0) {
            medicineHtml += `
                <div class="mt-4 bg-yellow-50 p-4 rounded-lg border border-yellow-200">
                    <h4 class="font-semibold text-yellow-800">Important Warnings:</h4>
                    <ul class="list-disc list-inside text-sm text-yellow-700 mt-2">
                        ${recommendations.warnings.map(warning => `<li>${warning}</li>`).join('')}
                    </ul>
                </div>
            `;
        }

        medicineHtml += '</div>';
        medicineRecsDiv.innerHTML = medicineHtml;
    } else {
        // If no medicines but have precautions, show those
        if (recommendations.precautions && recommendations.precautions.length > 0) {
            let precautionsHtml = `
                <div class="bg-blue-50 p-4 rounded-lg border border-blue-200">
                    <h4 class="font-semibold text-blue-800">Recommended Precautions:</h4>
                    <ul class="list-disc list-inside text-sm text-blue-700 mt-2">
                        ${recommendations.precautions.map(precaution => `
                            <li>${precaution.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</li>
                        `).join('')}
                    </ul>
                </div>
            `;
            medicineRecsDiv.innerHTML = precautionsHtml;
        } else {
            medicineRecsDiv.innerHTML = '<p class="text-gray-500">No specific medicine recommendations available.</p>';
        }
    }

    // Display Exercise Recommendations
    const exerciseRecsDiv = document.getElementById('exerciseRecommendations');
    if (recommendations.exercises && recommendations.exercises.length > 0) {
        let exerciseHtml = '<div class="space-y-4">';
        
        // Display intensity guidelines if available
        if (recommendations.intensity_guidelines) {
            const guidelines = recommendations.intensity_guidelines;
            exerciseHtml += `
                <div class="bg-green-50 p-4 rounded-lg border border-green-200 mb-4">
                    <h4 class="font-semibold text-green-800 mb-2">Exercise Intensity Guidelines</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <ul class="list-none text-sm text-green-700">
                                <li class="mb-2"><span class="font-medium">💓 Heart Rate:</span> ${guidelines.heart_rate}</li>
                                <li class="mb-2"><span class="font-medium">🫁 Breathing:</span> ${guidelines.breathing}</li>
                                <li class="mb-2"><span class="font-medium">⏱️ Duration:</span> ${guidelines.duration}</li>
                                <li class="mb-2"><span class="font-medium">📅 Frequency:</span> ${guidelines.frequency}</li>
                            </ul>
                        </div>
                        ${guidelines.signs_too_much ? `
                            <div>
                                <p class="font-medium text-yellow-700 mb-2">⚠️ Signs you're doing too much:</p>
                                <ul class="list-disc list-inside text-sm text-yellow-600">
                                    ${guidelines.signs_too_much.map(sign => `<li>${sign}</li>`).join('')}
                                </ul>
                            </div>
                        ` : ''}
                    </div>
                </div>
            `;
        }

        // Display exercise recommendations
        exerciseHtml += '<div class="grid grid-cols-1 md:grid-cols-2 gap-4">';
        recommendations.exercises.forEach(exercise => {
            const parts = exercise.split('\n');
            const [title, ...details] = parts;
            
            exerciseHtml += `
                <div class="bg-white p-4 rounded-lg shadow">
                    <h4 class="font-semibold text-gray-800 mb-3">${title}</h4>
                    <div class="space-y-2 text-sm">
                        ${details.map(detail => {
                            if (detail.trim()) {
                                const [label, content] = detail.split(': ');
                                let icon = '📝'; // Default icon
                                if (label.includes('Instructions')) icon = '✨';
                                if (label.includes('Benefits')) icon = '💪';
                                if (label.includes('Precautions')) icon = '⚠️';
                                return `<p class="text-gray-600">
                                    <span class="font-medium">${icon} ${label}:</span> ${content}
                                </p>`;
                            }
                            return '';
                        }).join('')}
                    </div>
                </div>
            `;
        });
        exerciseHtml += '</div>';

        // Display exercise warnings if any
        if (recommendations.exercise_warnings && recommendations.exercise_warnings.length > 0) {
            exerciseHtml += `
                <div class="mt-4 bg-yellow-50 p-4 rounded-lg border border-yellow-200">
                    <h4 class="font-semibold text-yellow-800 mb-2">⚠️ Exercise Precautions</h4>
                    <ul class="list-disc list-inside text-sm text-yellow-700">
                        ${recommendations.exercise_warnings.map(warning => `<li>${warning}</li>`).join('')}
                    </ul>
                </div>
            `;
        }

        // Display exercise progression plan if available
        if (recommendations.exercise_progression && recommendations.exercise_progression.length > 0) {
            exerciseHtml += `
                <div class="mt-6">
                    <h4 class="font-semibold text-gray-800 mb-4">📈 Exercise Progression Plan</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        ${recommendations.exercise_progression.map((week, index) => `
                            <div class="bg-blue-50 p-4 rounded-lg border border-blue-200">
                                <p class="text-blue-800"><span class="font-medium">Week ${index + 1}:</span> ${week.split(': ')[1]}</p>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }

        exerciseHtml += '</div>';
        exerciseRecsDiv.innerHTML = exerciseHtml;
    } else {
        exerciseRecsDiv.innerHTML = '<p class="text-gray-500">No specific exercise recommendations available.</p>';
    }

    // Display Diet Recommendations
    const dietRecsDiv = document.getElementById('dietRecommendations');
    if (recommendations.diet && recommendations.diet.length > 0) {
        let dietHtml = `
            <ul class="list-disc list-inside space-y-2">
                ${recommendations.diet.map(rec => `<li class="text-gray-700">${rec}</li>`).join('')}
            </ul>
        `;
        dietRecsDiv.innerHTML = dietHtml;
    } else {
        dietRecsDiv.innerHTML = '<p class="text-gray-500">No specific diet recommendations available.</p>';
    }

    // Display Lifestyle Recommendations
    const lifestyleRecsDiv = document.getElementById('lifestyleRecommendations');
    if (recommendations.lifestyle && recommendations.lifestyle.length > 0) {
        let lifestyleHtml = `
            <ul class="list-disc list-inside space-y-2">
                ${recommendations.lifestyle.map(rec => `<li class="text-gray-700">${rec}</li>`).join('')}
            </ul>
        `;
        lifestyleRecsDiv.innerHTML = lifestyleHtml;
    } else {
        lifestyleRecsDiv.innerHTML = '<p class="text-gray-500">No specific lifestyle recommendations available.</p>';
    }
} 