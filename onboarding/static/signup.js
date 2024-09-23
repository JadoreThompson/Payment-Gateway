document.addEventListener('DOMContentLoaded', function(){
    const baseURL = "http://127.0.0.1:5000/";
    const errorContainer = document.querySelector('.error-container');
    const signupForm = document.getElementById('signupForm');

    // Login Form listener
    signupForm.addEventListener('submit', async function(e){
        e.preventDefault();
        let message;
        console.log('submit');
        const formData = new FormData(signupForm);
        let formObj = {};
        for (let [k, v] of formData.entries()){
            formObj[k] = v;
        }

        console.log("Form OBJ: ", formObj);

        try {
            const rsp = await fetch(baseURL + "auth/signup", {
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