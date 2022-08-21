<template>

		<div class="login-screen">
			<div class="app-title">
				<h1>Login</h1>
			</div>

			<form @submit.prevent="submitForm" class="login-form">
				<div class="control-group">
				<input v-model="username" type="username" class="login-field" placeholder="Username" id="login-name">
				<label class="login-field-icon fui-user" for="login-name"></label>
				</div>

				<div class="control-group">
				<input v-model="password" type="password" class="login-field" placeholder="Password" id="login-pass" >
				<label class="login-field-icon fui-lock" for="login-pass"></label>
				</div>
                <button class="btn" type="submit">Login</button>
				
				<a class="login-link" href="#">Lost your password?</a>
			</form>
		</div>

</template>

<script>
import axios from 'axios';
export default {
    name: 'LoginForm',
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
                // Push to App dashboard
                this.$router.push("/dashboard");
                
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

.login-screen {
background-color: $background-color-2;
box-sizing: border-box;
padding: 20px;
border-radius: 5px;
border: 1px solid $border-color-1;
height: 400px;
width: 300px;
box-shadow: 0px 8px 9px -1px rgba(0,0,0,0.58);
-webkit-box-shadow: 0px 8px 9px -1px rgba(0,0,0,0.58);
-moz-box-shadow: 0px 8px 9px -1px rgba(0,0,0,0.58);
}

.app-title {
text-align: center;
color: $white;
}

.login-form {
text-align: center;
position: relative;
top: 20px;
}
.control-group {
margin-bottom: 10px;
}

input {
text-align: center;
background-color: transparent;
border: 1px solid $border-color-1;
border-radius: 3px;
font-size: 15px;
font-weight: 200;
padding: 10px 0;
width: 250px;
transition: border .5s;
margin-bottom: 10px;
color: $white;


}

input:hover {
border: 1px solid $border-color-hover;
box-shadow: none;
}
input:focus {
border: 1px solid $border-color-hover;
box-shadow: none;
outline: none;
}

.btn {
  
  border: 1px solid $border-color-1;
  background-color: $background-color-2;
  color: #ffffff;
  font-size: 16px;
  line-height: 25px;
  padding: 10px 0;
  text-decoration: none;
  text-shadow: none;
  border-radius: 3px;
  box-shadow: none;
  transition: 0.25s;
  display: block;
  width: 250px;
  margin: 0 auto;
  font-weight: 500;
}

.btn:hover {
  background-color: $border-color-1;
}

.login-link {
  font-size: 12px;
  color: $white;
  display: block;
	margin-top: 12px;
}
</style>