function showpotter(potter) {
    // Hide all content divs
    var contents = document.querySelectorAll('.content');
    contents.forEach(function(content) {
        content.style.display = 'none';
    });
    // Show the selected fruit content
    document.getElementById(potter + 'Content').style.display = 'block';
}