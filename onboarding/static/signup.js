document.addEventListener('DOMContentLoaded', function(){
    const baseURL = "http://127.0.0.1:5000/";
    const errorContainer = document.querySelector('.error-container');
    const signupForm = document.getElementById('signupForm');

    // Signup Form listener
    signupForm.addEventListener('submit', async function(e){
        e.preventDefault();
        let message;
        const formData = new FormData(signupForm);
        let formObj = {};
        for (let [k, v] of formData.entries()){
            if (k != 'csrfmiddlewaretoken') {
                formObj[k] = v;
            }
        }

        formObj['tos_acceptance'] = formObj['tos_acceptance'] === 'true';

        try {
            console.log(baseURL + "auth/signup");
            const rsp = await fetch(baseURL + "auth/signup", {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(formObj)
            });
            const data = await rsp.json();
            if (rsp.status != 200){
                throw new Error(data["message"]);
            }

            window.location.href = '/onboarding';

        } catch(e) {
            document.getElementById('error-message').textContent = e.message;
            errorContainer.style.display = 'block';
        }
    });
});