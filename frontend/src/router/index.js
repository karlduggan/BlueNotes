import { createRouter, createWebHistory } from "vue-router";
// Import the home page for router
import HomePage from '@/views/HomePage.vue';
import ToDoList from '@/views/ToDoList';
import DevPage from '@/views/DevPage';
import LogIn from '@/views/LogIn'
import SignUp from '@/views/SignUp'

const routes = [
    {
        path: '/', 
        name: 'HomePage', 
        component: HomePage
    },
    {
        path: '/logIn', 
        name: 'Login', 
        component: LogIn
    },
    {
        path: '/sign-up', 
        name: 'SignUp', 
        component: SignUp
    },
    {
        path: '/todo-list', 
        name: 'ToDoList', 
        component: ToDoList
    },
    {
        path: '/dev', 
        name: 'DevPage', 
        component: DevPage
    }
]

const router = createRouter( {
    history: createWebHistory(),
    routes
    
})

export default router