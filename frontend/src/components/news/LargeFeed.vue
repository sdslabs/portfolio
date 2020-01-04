<template>
    <div class="sm:w-feed h-auto shadow-feed pt-10">
        <div class="pl-10">
            <Label :text="event.types" />
        </div>
        <div class="flex flex-col h-auto mt-12 pb-12 pl-10 pr-navbar">
            <div class="font-extrabold text-xl leading-180">
                {{ event.title.toUpperCase() }}
            </div>
            <div class="mt-8 text-base font-semibold leading-170">
                {{ event.timing }}
            </div>
            <div class="mt-16 text-base leading-normal">
                {{ event.description }}
            </div>
        </div>
        <div v-if="eventUpdates.length != 0">
            <div class="font-semibold text-base pt-14 leading-170 pl-10 border-t-feed border-border pr-navbar">
                {{ eventUpdates.length }} Updates
            </div>
            <div
                class="flex flex-col pb-10 pl-10 pr-navbar"
                v-for="eventUpdates in eventUpdates"
                v-bind:key="eventUpdates.title"
            >
                <UpdateCard
                    :title="eventUpdates.title"
                    :url="eventUpdates.url"
                    :timing="eventUpdates.timing"
                    :description="eventUpdates.description"
                />
            </div>
        </div>
        <div class="pt-10 font-extrabold text-base pb-8 leading-170 pl-10 border-border border-t-feed">
            <router-link
                :to="'/news/'+event.title"
                :class="'no-underline inline-block text-'+ colors[index]"
            >
                Know More
            </router-link>
        </div>
    </div>
</template>

<script>
import Label from "@/components/Label.vue";
import UpdateCard from "@/components/news/UpdateCard.vue";
import { CONFIG } from "@/utils/constants.js";
export default {
    name: "largefeed",
    components: {
        Label,
        UpdateCard
    },
    data: function initData() {
        return {
            index: Date.now() % 6,
            colors: CONFIG.colors
        };
    },
    props: {
        event: Object,
        eventUpdates: Array
    }
};
</script>
