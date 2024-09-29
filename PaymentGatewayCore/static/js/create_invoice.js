document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('save-draft').addEventListener('click', function(){
        document.getElementById('draft').value = "true";
        document.querySelector('form').submit();
    });
});