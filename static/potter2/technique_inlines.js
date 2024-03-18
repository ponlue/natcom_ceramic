document.addEventListener('DOMContentLoaded', function() {

    let techniqueForm = document.querySelectorAll(".technique-form")
    let container = document.querySelector("#technique-form-container")
    let addButton = document.querySelector("#add-technique-form-btn")
    let totalForms = document.querySelector("#id_potter-TOTAL_FORMS")

    let formNum = techniqueForm.length // count len of technique making pottery form

    addButton.addEventListener('click', addForm)

    function addForm(e) {
        e.preventDefault()

        let formTemplate = document.querySelector(".technique-form").cloneNode(true)

        formTemplate.querySelectorAll('input, textarea').forEach(function(field) {
            let newId = field.id.replace(/-\d+-/, `-${formNum}-`)
            let newName = field.name.replace(/-\d+-/, `-${formNum}-`)

            field.value = ''  // Clear field value
            field.id = newId  // Update input ID
            field.name = newName  // Update input name
        })

        formTemplate.querySelectorAll('label').forEach(function(label) {
            let newFor = label.getAttribute('for').replace(/-\d+-/, `-${formNum}-`)
            label.setAttribute('for', newFor)  // Update label 'for' attribute
            label.innerHTML = label.innerHTML.replace(/#\d+/g, `#${formNum}`) // Update label text
        })

        container.appendChild(formTemplate)

        formNum++;  // Increment form number
        totalForms.value = formNum;  // Update the total forms value
    }
});