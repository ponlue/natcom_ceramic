document.addEventListener("DOMContentLoaded", function() {
    const addImageButton = document.getElementById("add-image-form-btn");
    const imageFormContainer = document.getElementById("image-form-container");
    let formIndex = document.querySelectorAll(".image-form").length; // Initial form index based on existing forms
    const totalFormsInput = document.getElementById("id_image_set-TOTAL_FORMS");

    addImageButton.addEventListener("click", function() {
        const newImageForm = document.createElement("div");
        newImageForm.classList.add("image-form");
        
        const label = document.createElement("label");
        label.setAttribute("for", `id_image_set-${formIndex}-image`);
        label.textContent = "រូបភាពស្មូន / Potter Image:";
        
        const fileInput = document.createElement("input");
        fileInput.setAttribute("type", "file");
        fileInput.setAttribute("name", `image_set-${formIndex}-image`);
        fileInput.setAttribute("accept", "image/*");
        fileInput.setAttribute("id", `id_image_set-${formIndex}-image`);
        
        const hiddenPotterInput = document.createElement("input");
        hiddenPotterInput.setAttribute("type", "hidden");
        hiddenPotterInput.setAttribute("name", `image_set-${formIndex}-potter`);
        hiddenPotterInput.setAttribute("id", `id_image_set-${formIndex}-potter`);
        
        const hiddenIdInput = document.createElement("input");
        hiddenIdInput.setAttribute("type", "hidden");
        hiddenIdInput.setAttribute("name", `image_set-${formIndex}-id`);
        hiddenIdInput.setAttribute("id", `id_image_set-${formIndex}-id`);
        
        newImageForm.appendChild(label);
        newImageForm.appendChild(fileInput);
        newImageForm.appendChild(hiddenPotterInput);
        newImageForm.appendChild(hiddenIdInput);
        
        imageFormContainer.appendChild(newImageForm);
        
        formIndex++; // Increment form index for the next form
        totalFormsInput.value = formIndex; // Update TOTAL_FORMS value
    });
});
