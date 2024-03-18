document.addEventListener('DOMContentLoaded',function(){let imageForm=document.querySelectorAll(".image-form")
let container=document.querySelector("#image-form-container")
let addButton=document.querySelector("#add-image-form-btn")
let totalForms=document.querySelector("#id_form-TOTAL_FORMS")
let formNum=imageForm.length
addButton.addEventListener('click',addForm)
function addForm(e){e.preventDefault()
let newForm=imageForm[0].cloneNode(true)
let formRegex=new RegExp(`image_set-(\\d+)-`,'g')
let newHtml=newForm.innerHTML.replace(formRegex,`image_set-${formNum}-`)
newForm.innerHTML=newHtml
let inputs=newForm.querySelectorAll('input[type="file"]')
inputs.forEach(function(input){input.value=''
input.id=`id_image_set-${formNum}-image`
input.name=`image_set-${formNum}-image`})
container.appendChild(newForm)
formNum++;totalForms.value=formNum;}});;document.addEventListener('DOMContentLoaded',function(){let techniqueForm=document.querySelectorAll(".technique-form")
let container=document.querySelector("#technique-form-container")
let addButton=document.querySelector("#add-technique-form-btn")
let totalForms=document.querySelector("#id_form-TOTAL_FORMS")
let formNum=techniqueForm.length
addButton.addEventListener('click',addForm)
function addForm(e){e.preventDefault()
let newForm=imageForm[0].cloneNode(true)
let formRegex=new RegExp(`__prefix__`,'g')
let newId=formNum;let newHtml=newForm.innerHTML.replace(formRegex,newId)
newForm.innerHTML=newHtml
let fields=newForm.querySelectorAll('input, textarea')
fields.forEach(function(field){field.value=''
field.id=field.id.replace(formRegex,newId)
field.name=field.name.replace(formRegex,newId)})
container.appendChild(newForm)
formNum++;totalForms.value=formNum;}});;