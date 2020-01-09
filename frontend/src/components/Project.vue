<template>
    <div
        class="pt-navbar sm:h-screen flex justify-end items-center"
        :id="permalink"
    >
        <div
            class="project-wrapper sm:w-5/6 flex flex-col-reverse sm:flex-row justify-center sm:items-center"
        >
            <div class="mt-20 sm:mt-0 sm:w-4/10 sm:pr-16">
                <h2 class="uppercase font-bold text-3xl leading-170 pb-12">
                    {{ title }}
                </h2>
                <p class="text-base leading-160">{{ desc }}</p>
                <div class="text-sm pt-16">
                    <Button v-bind:native="true" :url="url" text="Open App" />
                </div>
            </div>
            <div class="-ml-6 flex sm:-ml-0 sm:pl-24 sm:w-7/10">
                <div class="self-center flex flex-row z-10">
                    <img class="w-full z-20" :src="image_url" />
                    <div
                        :class="
                            'w-140 h-140 sm:h-120 self-end -mr-16 -ml-5/10 sm:-mr-26 bg-' +
                                colors[index]
                        "
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Button from "@/components/Button.vue";
import { CONFIG } from "@/utils/constants.js";

export default {
    name: "project",
    props: {
        title: {
            type: String,
            required: true
        },
        desc: {
            type: String,
            required: true
        },
        url: {
            type: String,
            required: true
        },
        image_url: {
            type: String,
            required: true
        },
        permalink: {
            type: String,
            required: true
        }
    },
    components: {
        Button
    },
    data: function initData() {
        return {
            index: Date.now() % 6,
            colors: CONFIG.colors
        };
    }
};
</script>
