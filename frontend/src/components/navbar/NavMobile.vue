<template>
    <div
        v-bind:class="{
            'bg-grey': open,
            'bg-transparent': !open,
            navhide: !open && !active
        }"
        class="fixed h-full w-full z-30 sm:hidden"
        @click="close"
    >
        <nav
            v-bind:class="{
                nav: open,
                navclose: !open && active,
                navhide: !open && !active
            }"
            class="fixed h-full bg-white w-3/4 ml-1/4 flex flex-col"
        >
            <div class="self-end mt-16 mr-23 h-8 w-8">
                <img src="@/assets/images/close.svg" />
            </div>
            <div
                class="text-lg text-black leading-normal justify-center mt-20 pl-12 pr-12"
            >
                <NavLink
                    class="py-6"
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/projects"
                    text="PROJECTS"
                    @click="close"
                />
                <NavLink
                    class="py-6"
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/news"
                    text="NEWS"
                    @click="close"
                />
                <NavLink
                    class="py-6"
                    v-bind:native="true"
                    v-bind:last="false"
                    url="https://blog.sdslabs.co/"
                    text="BLOG"
                    @click="close"
                />
                <NavLink
                    class="py-6"
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/about"
                    text="ABOUT US"
                    @click="close"
                />
                <NavLink
                    class="py-6"
                    v-bind:native="true"
                    v-bind:last="true"
                    url="/contact"
                    text="CONTACT"
                    @click="close"
                />
            </div>
            <!-- <div class="text-sm mt-14 ml-12 mr-12">
                <Button
                    v-if="!$store.state.login"
                    class="w-full h-24 pb-20 text-center text-lg"
                    v-bind:native="true"
                    url="https://accounts.sdslabs.co/"
                    text="Login"
                    @click="close"
                />
                <div v-else>
                    <div class="flex flex-row items-center mt-4 pb-7">
                        <div
                            class="flex items-center justify-center h-20 w-20 rounded-50 bg-black text-white content-center font-bold text-2xl"
                        >
                            {{ this.name[0].toLowerCase() }}
                        </div>
                        <div
                            class="ml-7 text-black font-extrabold font-sans text-xl"
                        >
                            {{ this.name.toUpperCase() }}
                        </div>
                    </div>
                    <div class="h-18 flex flex-row bg-team mt-7">
                        <div class="ml-6">
                            <img src="@/assets/images/logo-square.svg" />
                        </div>
                        <div
                            class="flex items-center font-sans font-semibold text-lg ml-6 mr-6"
                        >
                            <a
                                class="no-underline text-black"
                                rel="noreferrer noopener"
                                href="https://accounts.sdslabs.co/"
                                >Open SDSLabs Account</a
                            >
                        </div>
                    </div>
                    <div
                        class="logout font-sans text-xl mt-16 mb-8 cursor-pointer"
                        @click="logout"
                    >
                        Logout
                    </div>
                </div>
            </div> -->
        </nav>
    </div>
</template>

<script>
import NavLink from "@/components/navbar/NavLink.vue";
// import Button from "@/components/Button.vue";
import { LOGOUT } from "@/mutation-types";
// import { config } from "@/config/config";
// import API from "falcon-client-js";

export default {
    name: "NavMobile",
    components: {
        NavLink
        // Button
    },
    props: {
        open: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {
            active: false,
            name: ""
        };
    },
    methods: {
        close() {
            this.active = true;
            this.$emit("click");
            setTimeout(() => {
                let vm = this;
                vm.active = false;
            }, 500);
        },
        logout() {
            this.$store.dispatch(LOGOUT);
        }
    },
    created() {
        // const client = new API.API(config);
        // client.get_logged_in_user(getCookie("sdslabs")).then(user => {
        //     console.log(user);
        // });
        //Do something to fetch user details
    }
};
</script>

<style lang="scss" scoped>
@keyframes slideIn {
    0% {
        transform: translate(100%, 0%);
        opacity: 1;
    }
    100% {
        transform: translate(0%, 0%);
        opacity: 1;
    }
}
@keyframes slideOut {
    0% {
        transform: translate(0%, 0%);
        opacity: 1;
    }
    100% {
        transform: translate(100%, 0%);
        opacity: 1;
        display: none;
    }
}
.nav {
    animation: slideIn 0.5s ease forwards;
}
.navclose {
    animation: slideOut 0.5s ease forwards;
}
.navhide {
    display: none;
}
</style>
