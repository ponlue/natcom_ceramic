document.addEventListener("DOMContentLoaded", function() {
    const addTechniqueButton = document.getElementById("add-technique-form-btn");
    const techniqueFormContainer = document.getElementById("technique-form-container");
    let formIndex = 0; // Initial form index
    
    addTechniqueButton.addEventListener("click", function() {
        formIndex++;
        const newTechniqueForm = document.createElement("div");
        newTechniqueForm.classList.add("technique-form");
        newTechniqueForm.innerHTML = `
            <label for="id_potter-${formIndex}-title">ចំណងជើង / Title:</label>
            <input type="text" name="potter-${formIndex}-title" maxlength="200" id="id_potter-${formIndex}-title">
            
            <label for="id_potter-${formIndex}-description">ពិពណ៌នា / Description:</label>
            <div class="ck-editor-container">
                <textarea name="potter-${formIndex}-description" class="django_ckeditor_5" resize="vertical" rows="8" id="id_potter-${formIndex}-description"></textarea>
                <span class="word-count" id="id_potter-${formIndex}-description_script-word-count"></span>
            </div>
            <input type="hidden" id="id_potter-${formIndex}-description_script-ck-editor-5-upload-url" data-upload-url="/ckeditor5/image_upload/" data-csrf_cookie_name="csrftoken">
            <span><script id="id_potter-${formIndex}-description_script" type="application/json">{"toolbar": ["heading", "|", "bold", "italic", "link", "bulletedList", "numberedList", "blockQuote", "imageUpload"]}</script></span>
            
            <label for="id_potter-${formIndex}-image">រូបនៃការផលិត / Photo:</label>
            <input type="file" name="potter-${formIndex}-image" accept="image/*" id="id_potter-${formIndex}-image">
            <input type="hidden" name="potter-${formIndex}-potter" id="id_potter-${formIndex}-potter">
            <input type="hidden" name="potter-${formIndex}-id" id="id_potter-${formIndex}-id">
        `;
        
        techniqueFormContainer.appendChild(newTechniqueForm);
        
        // Update TOTAL_FORMS value
        document.getElementById("id_potter-TOTAL_FORMS").value = formIndex + 1;
    });
});
