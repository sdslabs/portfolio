import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueFullPage from "vue-fullpage.js";

import "@/assets/css/tailwind.css";

Vue.config.productionTip = false;
Vue.use(VueFullPage);

new Vue({
    el: "#fullpage-home",
    name: "app",
    data: function(){
        return {
            options: {
                afterLoad: this.afterLoad,
                navigation: true,
                scrollBar: false,
                controlArrows: true,
                anchors: ['page1', 'page2', 'page3'],
            },
        }
    },
    methods: {
        afterLoad: function(origin, destination, direction){
            console.log("After load....");
            console.log(destination);
        }
    }
});

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount("#app");
