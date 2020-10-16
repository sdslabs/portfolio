<template>
    <div class="w-full pt-38 overflow-x-hidden" @click="close">
        <div class="flex flex-col sm:flex-row">
            <div class="sm:pt-72">
                <img
                    class="h-32 -ml-32 sm:w-188 sm:h-44 sm:ml-0"
                    src="@/assets/images/error-left.svg"
                />
            </div>
            <div class="">
                <img
                    class=" hidden sm:block sm:w-212 sm:h-140"
                    src="@/assets/images/404.svg"
                />
            </div>
            <div class="pt-14 flex justify-center">
                <img class=" sm:hidden" src="@/assets/images/404.png" />
            </div>
            <div class="pt-12 sm:pt-72">
                <img
                    class=" h-32 ml-64 sm:ml-0 sm:w-216 sm:h-44"
                    src="@/assets/images/error-right.svg"
                />
            </div>
        </div>
        <div
            class=" pt-48 text-lg sm:pt-20 font-semibold leading-normal sm:text-2xl text-center"
        >
            Something went wrong... please try again
        </div>
        <div class="text-center">
            <button
                class="w-96 h-26 sm:w-72 sm:h-20 bg-error mt-16 sm:mt-20 p-4 leading-170 text-lg sm:text-base font-extrabold text-white"
                onclick="location.href = '/';"
            >
                Go to Home
                <span class=" sm:inline-block sm:h-full sm:align-middle">
                    <img
                        class="pl-8 -mb-2"
                        src="@/assets/images/button-arrow.svg"
                    />
                </span>
            </button>
        </div>
    </div>
</template>

<script>
import { CLOSE_USER } from "@/mutation-types";

export default {
    name: "Error404",
    methods: {
        close() {
            this.$store.commit(CLOSE_USER);
        }
    }
};
</script>
