import { createStore } from "vuex";

export default createStore({
    state: {
        name: "Testing Vue State Management in store/index.js",
        taskList: []
    },
    mutations: { // Synchronous
        addTask(state,payload){
            state.taskList.push(payload);
        },
        addData(state, payload){
            state.taskList = payload;
        }
    },
    actions: { // Asynchronous
        addTask(state, payload){
            // To invoke the action, call on the store.dispatch() function:
            state.commit('addTask', payload)
        },
        addData(state, payload){
            state.commit('addData', payload)
        }

    },
    getters: {
        getTaskList(state){
            return state.taskList;
        }
    },
    modules: {
        

    }
})