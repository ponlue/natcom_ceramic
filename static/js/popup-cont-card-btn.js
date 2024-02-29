// document.getElementById('toggleButton-video').onclick = function() {
//     document.getElementById('popupContainer-video').style.display = 'block';
// };

// document.getElementById('closeButton-video').onclick = function() {
//     document.getElementById('popupContainer-video').style.display = 'none';
// };

// document.getElementById('toggleButton-image').onclick = function() {
//     document.getElementById('popupContainer-image').style.display = 'block';
// };

// document.getElementById('closeButton-image').onclick = function() {
//     document.getElementById('popupContainer-image').style.display = 'none';
// };



// function togglePopup(toggleButtonId, closeButtonId, popupContainerId) {
//     var toggleButton = document.getElementById(toggleButtonId);
//     var closeButton = document.getElementById(closeButtonId);
//     var popupContainer = document.getElementById(popupContainerId);

//     toggleButton.onclick = function() {
//         popupContainer.style.display = 'block';
//     };

//     closeButton.onclick = function() {
//         popupContainer.style.display = 'none';
//     };
// }

// // Call the function for video pop-up
// togglePopup('toggleButton-video', 'closeButton-video', 'popupContainer-video');

// // Call the function for image pop-up
// togglePopup('toggleButton-image', 'closeButton-image', 'popupContainer-image');


function togglePopup(toggleButtonsClass, closeButtonsClass, popupContainersClass) {
    var toggleButtons = document.getElementsByClassName(toggleButtonsClass);
    var closeButtons = document.getElementsByClassName(closeButtonsClass);
    var popupContainers = document.getElementsByClassName(popupContainersClass);

    for (var i = 0; i < toggleButtons.length; i++) {
        toggleButtons[i].onclick = function() {
            var index = Array.prototype.indexOf.call(toggleButtons, this);
            popupContainers[index].style.display = 'block';
        };
    }

    for (var j = 0; j < closeButtons.length; j++) {
        closeButtons[j].onclick = function() {
            var index = Array.prototype.indexOf.call(closeButtons, this);
            popupContainers[index].style.display = 'none';
        };
    }
}

// Call the function for video pop-up
togglePopup('btn-click-vid', 'close', 'popup-container');

// Call the function for image pop-up
togglePopup( 'btn-click-img','close', 'popup-container');
