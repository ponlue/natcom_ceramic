// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();



// owl carousel slider js
var owl = $('.project_carousel').owlCarousel({
    loop: false,
    margin: 15,
    center: true,
    startPosition: 2,
    autoplay: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    autoplayHoverPause: true,
    responsive: {
        0: {
            center: false,
            items: 1,
            margin: 0
        },
        769: {
            items: 2,
        },
        992: {
            center: true,
            items: 3
        }
    }
})


// owl.owlcarousel2_filter

$('.owl-filter-bar').on('click', '.item', function (e) {
    var $items = $('.owl-filter-bar a')
    var $item = $(this);
    var filter = $item.data('owl-filter')
    $items.removeClass("active");
    $item.addClass("active");
    owl.owlcarousel2_filter(filter);

    e.preventDefault();
})
/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}



// Image preview
function previewImages(input) {
    var previewContainer = document.getElementById('preview-container');
    previewContainer.innerHTML = '';

    if (input.files) {
        var filesAmount = input.files.length;

        for (var i = 0; i < filesAmount; i++) {
            var reader = new FileReader();

            reader.onload = function (event) {
                var container = document.createElement('div');
                container.className = 'preview-image-container';

                var img = document.createElement('img');
                img.setAttribute('src', event.target.result);
                img.className = 'preview-image';
                img.onclick = function() {
                    openLightbox(event.target.result);
                };

                var deleteIcon = document.createElement('span');
                deleteIcon.innerHTML = '&#10060;';
                deleteIcon.className = 'delete-icon';
                deleteIcon.onclick = function() {
                    container.remove();
                };

                container.appendChild(img);
                container.appendChild(deleteIcon);

                previewContainer.appendChild(container);
            }

            reader.readAsDataURL(input.files[i]);
        }
    }
}

function openLightbox(imageSrc) {
    var lightbox = document.getElementById('lightbox');
    var lightboxImage = document.getElementById('lightbox-image');
    lightboxImage.src = imageSrc;
    lightbox.style.display = 'flex';
}

function closeLightbox() {
    var lightbox = document.getElementById('lightbox');
    lightbox.style.display = 'none';
}

// End image preview