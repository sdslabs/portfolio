<template>
    <div class="pt-navbar h-screen flex justify-end items-center">
        <div class="project-wrapper sm:w-9/10 flex flex-col sm:flex-row justify-center items-center">
            <div class="sm:w-1/3">
                <h2 class="uppercase font-bold text-3xl leading-170 pb-12">{{ title }}</h2>
                <p class="text-base leading-160">{{ desc }}</p>
                <div class="text-sm pt-16">
                    <Button v-bind:native=true :url="url" text="OPEN APP" />
                </div>
            </div>
            <div class="-ml-6 sm:-ml-0 sm:pl-44 sm:w-2/3">
                <img class="w-full" :src="image_url" />
            </div>
        </div>
    </div>
</template>

<script>
import Button from "@/components/Button.vue";

export default {
    name: "project",
    props: {
        title: String,
        desc: String,
        url: String,
        image_url: String
    },
    components: {
        Button
    }
};
</script>
