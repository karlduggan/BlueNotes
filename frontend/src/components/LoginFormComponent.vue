<template>
    <div class="form-container">
        <h1>Login</h1>
        <form @submit.prevent="submitForm">
            <input type="username" name="username" v-model="username">
            <input type="password" name="password" v-model="password">
            <button type="submit">Log In</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'LoginFormComponent',
    data(){
        return {
            usernmae: "",
            password: ""
        }
    }, 
    methods: {
        submitForm: function () {
            const formData = {
                username: this.username,
                password: this.password
            };
            axios
                .post("/api/v1/token/login", formData)
                .then(response => {
                console.log(response);
                // Get token
                const token = response.data.auth_token;
                // Set token
                this.$store.dispatch(token);
                axios.defaults.headers.common["Authorization"] = "Token " + token;
                // store token to the locaStorage
                localStorage.setItem("token", token);
                // Push to App
                this.$router.push("/todo-list");
                // Set the username for welcome feature
                this.$store.state.username = this.username
                localStorage.setItem('username', this.username)
            })
                .catch(error => {
                console.log(error);
            });
        }
    }
}
</script>

<style lang="scss" scoped>
.form-container {
    background-color: $background-color-3;
    width: 450px;
    height: 600px;
    border: 1px solid $border-color-1;

    box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.5)  ; 
    -webkit-box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.5)  ; 
    -moz-box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.5)  ; 

}
.form-container h1 {
    text-align: center;
    color: $white;
}
</style>