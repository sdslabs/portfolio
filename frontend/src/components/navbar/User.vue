<template>
    <div>
        <div
            @click="toggle"
            class="user flex items-center justify-center h-12 w-12 rounded-50 bg-black text-white content-center font-bold cursor-pointer"
        >
            {{ this.name[0].toLowerCase() }}
        </div>
        <div
            v-if="$store.state.user"
            class="absolute flex flex-col mt-4 shadow-user -ml-80 bg-white"
        >
            <div class="flex flex-row items-center mt-7 mx-7 pb-7 border-b-1">
                <div
                    class="flex items-center justify-center h-12 w-12 rounded-50 bg-black text-white content-center font-bold"
                >
                    {{ this.name[0].toLowerCase() }}
                </div>
                <div class="ml-5 text-black font-extrabold font-sans">
                    {{ this.name.toUpperCase() }}
                </div>
            </div>
            <div class="h-12 w-80 flex flex-row bg-team mx-6 mt-7">
                <div class="ml-6">
                    <img src="@/assets/images/logo-square.svg" />
                </div>
                <div class="flex items-center font-sans text-xs ml-6 mr-6">
                    <a
                        class="no-underline text-black"
                        rel="noreferrer noopener"
                        href="https://accounts.sdslabs.co/"
                        >Open SDSLabs Account</a
                    >
                </div>
            </div>
            <div
                class="logout font-sans mt-7 ml-7 mb-8 cursor-pointer"
                @click="logout"
            >
                Logout
            </div>
        </div>
    </div>
</template>

<script>
import { TOGGLE_USER, LOGOUT } from "@/mutation-types";
import { config } from "@/config/config";
import API from "falcon-client-js";
import cookies from "js-cookie";

export default {
    name: "User",
    data() {
        return {
            name: ""
        };
    },
    methods: {
        toggle() {
            this.$store.commit(TOGGLE_USER);
        },
        logout() {
            this.$store.dispatch(LOGOUT);
        }
    },
    created() {
        const client = new API.API(config);
        client.get_logged_in_user(cookies).then(user => {
            console.log("createdd")
            console.log(user);
        });
    }
};
</script>
