document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('save-draft').addEventListener('click', function(){
        document.getElementById('draft').value = true;
        document.getElementById('draft').disabled = false;
    });
});