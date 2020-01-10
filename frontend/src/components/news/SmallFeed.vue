<template>
    <div class="sm:w-event h-auto shadow-feed pt-10">
        <div class="pl-10"><Label :text="event.types" /></div>
        <div class="flex flex-col mt-10 pb-10 pl-10 pr-10">
            <div class="font-extrabold text-xl leading-180">
                {{ event.title.toUpperCase() }}
            </div>
            <div class="mt-8 text-base text-grey font-semibold leading-170">
                {{ event.timing }}
            </div>
            <div class="mt-14 text-base text-grey leading-normal">
                {{ event.shortDescription }}
            </div>
        </div>
        <div
            class="pt-8 font-extrabold text-base pb-8 pl-10 border-t-feed border-border leading-170"
        >
            <a
                :href="event.url"
                target="_blank"
                :class="'no-underline inline-block text-' + colors[index]"
                >Check Now</a
            >
        </div>
    </div>
</template>

<script>
import Label from "@/components/Label.vue";
import { CONFIG } from "@/utils/constants.js";
export default {
    name: "smallfeed",
    components: {
        Label
    },
    data: function initData() {
        return {
            index: Date.now() % 6,
            colors: CONFIG.colors
        };
    },
    props: {
        event: Object
    }
};
</script>
