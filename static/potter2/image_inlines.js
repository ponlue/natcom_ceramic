document.addEventListener('DOMContentLoaded', function() {

    let imageForm = document.querySelectorAll(".image-form")
    let container = document.querySelector("#image-form-container")
    let addButton = document.querySelector("#add-image-form-btn")
    let totalForms = document.querySelector("#id_form-TOTAL_FORMS")

    let formNum = imageForm.length // count len of image form

    addButton.addEventListener('click', addForm)

    function addForm(e) {
        e.preventDefault()

        let newForm = imageForm[0].cloneNode(true)
        let formRegex = new RegExp(`image_set-(\\d+)-`, 'g')

        let newHtml = newForm.innerHTML.replace(formRegex, `image_set-${formNum}-`)
        newForm.innerHTML = newHtml

        let inputs = newForm.querySelectorAll('input[type="file"]')
        inputs.forEach(function(input) {
            input.value = ''  // Clear file input value
            input.id = `id_image_set-${formNum}-image`  // Update input ID
            input.name = `image_set-${formNum}-image`  // Update input name
        })

        container.appendChild(newForm)

        formNum++;  // Increment form number
        totalForms.value = formNum;  // Update the total forms value
    }
});