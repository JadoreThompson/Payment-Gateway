document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('save-draft').addEventListener('click', function(){
        console.log('clicked');
        document.getElementById('draft').value = "true";
        document.querySelector('form').submit();
        console.log(document.querySelector('form'));
    });
});