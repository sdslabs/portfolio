import Vue from "vue";
import Vuex from "vuex";
import { TOGGLE_USER, CLOSE_USER, LOGOUT } from "./mutation-types";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        login: true,
        user: false
    },
    mutations: {
        [TOGGLE_USER](state) {
            state.user = !state.user;
        },
        [CLOSE_USER](state) {
            if (state.user) state.user = false;
        }
    },
    actions: {
        [LOGOUT]({ state }) {
            state.login = false;
            state.user = false;
            // const cookieRemoveString =
            //     "sdslabs= ; expires = Thu, 01 Jan 1970 00:00:00 GMT; Domain=.sdslabs.co; path=/;";
            // document.cookie = cookieRemoveString;
        }
    }
});
