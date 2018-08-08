const titleInput = document.querySelector('input[name=title]');
const slugsInput = document.querySelector('input[name=slugs]');

const slugify = (val) => {

    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')         // Replace & with 'and'
        .replace(/[\s\W-]+/g, '-')      // Replace spaces, non-word characters and dashes with a single dash (-)

};

titleInput.addEventListener('keyup', (e) => {
    slugsInput.setAttribute('value', slugify(titleInput.value));
});
