<template>
    <nav>
        <img src="../assets/bluenotes_logo.png" alt="" srcset="" width="100">
        <div class="login-container" >
            <!-- Check user is authorized to access -->
            <div class="login-sign-out" v-if="!this.$store.state.isAuthenticated">
            <p><span>Hello </span></p>
                <button class="login-signout" @click="login()">Login</button>


            </div>
            <div class="login-sign-out"  v-else>
                <p><span>Welcome </span><span :style="`font-weight:bold`">{{this.$store.state.username}}</span></p>
                <button class="login-signout" @click="signOut()">Sign out</button>
            </div>
                
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavBarComponent",
    props: {
        title: String,
    },
    data(){
        return {
            username: ""
        }
    },
    methods: {
        signOut: function() {
            this.$store.dispatch('removeToken')
            // Remove username from local storage
            localStorage.removeItem('username')
            // Redirect the browser to the home landing page
            this.$router.push('/')
        },
        login: function() {
            // Redirect the browser to the login page
            this.$router.push('/login')
        }
    },
    mounted() {
        this.username = localStorage.getItem("username");
    }
}
</script>

<style lang="scss" scoped>
h1 {
    color: $white;
    margin: 0;
    padding: 15px;
}
nav {
    background-color: $background-color-3;
    border-bottom: 1px solid $border-color-1;

    width: 100%;
}
img {
    padding: 10px;
    position: relative;
    left: 30px;
}
.login-container {
    color: $white;
    position: absolute;
    padding: 16px;
    right: 20px;

}
.login-container {
    display: inline;

}

.login-sign-out {
    display: inline-flex;
    align-items: center;
}
.login-signout {
    position: relative;
    border: 1px solid $border-color-1;
    width: 100px;
    height: 30px;
    background: $background-color-3;
    color: $white;
    cursor: pointer;
    transition: background-color 100ms linear;
}
.login-signout:hover {
background-color: $border-color-1;
}
.login-sign-out p {
    margin: 15px;
}
</style>