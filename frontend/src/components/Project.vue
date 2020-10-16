<template>
    <div
        class="pt-60 sm:pt-navbar sm:h-screen flex justify-end items-center"
        :id="permalink"
    >
        <div
            class="project-wrapper sm:w-5/6 flex flex-col-reverse sm:flex-row justify-center sm:items-center"
        >
            <div class="mt-20 sm:mt-0 sm:w-4/10 sm:pr-16">
                <h2 class="uppercase font-black text-3xl leading-170 pb-12">
                    {{ title }}
                </h2>
                <p class="text-1.5xl text-grey sm:text-base leading-160">
                    {{ desc }}
                </p>
                <div class="text-sm pt-16">
                    <Button v-bind:native="true" :url="url" text="Open App" />
                </div>
            </div>
            <div class="-ml-6 flex sm:-ml-0 sm:pl-24 sm:w-7/10">
                <div class="image self-center flex flex-row z-10">
                    <img class="w-full z-20" :src="image_url" />
                    <div
                        :class="
                            'w-140 sm:w-100 h-180 sm:h-148 self-end -mr-16 -mt-14 -mb-14 sm:-mt-8 sm:-mb-8 -ml-5/10 sm:-mr-0 sm:mr-26 bg-' +
                                color
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
        },
        color: {
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
<style lang="scss" scoped>
.image {
    align-items: center;
}
</style>
