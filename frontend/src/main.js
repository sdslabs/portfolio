import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueFullPage from "vue-fullpage.js";

import "@/assets/css/tailwind.css";
import "@/assets/css/fullpage.min.css";

Vue.config.productionTip = false;
Vue.use(VueFullPage);

new Vue({
    el: "#app",
    name: "app",
    data: function(){
        return {
            options: {
                afterLoad: this.afterLoad,
                navigation: true,
                anchors: ['page1', 'page2', 'page3'],
                sectionsColor: ['#41b883', '#ff5f45', '#0798ec', '#fec401', '#1bcee6', '#ee1a59', '#2c3e4f', '#ba5be9', '#b4b8ab']
            },
        }
    },
    methods: {
        afterLoad: function(origin, destination, direction){
            console.log("After load....");
            console.log(destination);
        }
    },
    router,
    store,
    render: h => h(App)
}).$mount("#app");
