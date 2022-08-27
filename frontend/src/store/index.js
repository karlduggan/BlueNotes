import { createStore } from "vuex";

export default createStore({
    state: {
        // Checking authentication
        token: '',
        isAuthenticated: false,
        // Store api request results in the task list
        name: "Testing Vue State Management in store/index.js",
        projectList: [],
        ticketList: [],
        commentList:[],
        // Store the username
        username: "",
        showComments: false,
        // Tracking the selected project
        selectedProjectID: null,
        // Tracking current ticket selected 
        selectedTicketID: null,
        // Show Add Ticket Modal
        showAddTicketModal: false,
        // Show create project Modal
        createProjectDisplay: false
    },
    mutations: { // Synchronous
        // Authentication
        initializeStore(state) {
            if (localStorage.getItem('token'))
                {
                    state.token = localStorage.getItem('token')
                    state.isAuthenticated = true
                }
            else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
        },
        removeToken(state) {
            state.token = ''
            state.isAuthenticated = false
        },
        // Authentication END 
        addTicket(state,payload){
            state.ticketList.push(payload);
        },
        addData(state, payload){
            state.ticketList = payload;
        }
    },
    actions: { // Asynchronous
        addTicket(state, payload){
            // To invoke the action, call on the store.dispatch() function:
            state.commit('addTicket', payload)
        },
        addData(state, payload){
            state.commit('addData', payload)
        },
        // Authorization
        setToken(state, token){
            state.commit('setToken', token)
        },
        removeToken(state){
            state.commit('removeToken')
        }

    },
    getters: {
        getTicketList(state){
            return state.ticketList;
        }
    },
    modules: {
        

    }
})