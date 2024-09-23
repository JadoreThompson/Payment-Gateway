document.addEventListener('DOMContentLoaded', function(){
    const baseURL = "http://127.0.0.1:5000/";
    const errorContainer = document.querySelector('.error-container');
    const loginForm = document.getElementById('loginForm');

    // Login Form listener
    loginForm.addEventListener('submit', async function(e){
        e.preventDefault();
        let message;

        const formData = newFormData(loginForm);
        let formObj = {};
        for (let [k, v] of formData.entries()){
            formObj[k] = v;
        }

        console.log("Form OBJ: ", formObj);

        try {
            const rsp = await fetch(baseURL + "auth/login", {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: formObj
            });

            const data = await rsp.json();
            if (rsp.status == 200){
                window.location.href = '/auth/onboarding';
            } else {
                throw new Error(data['message']);
            }

        } catch(e) {
            document.getElementById('error-message').textContent = message;
            errorContainer.style.display = 'block';
        }
    });
});