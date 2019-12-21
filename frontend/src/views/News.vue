<template>
    <div class="flex flex-col pt-60 pl-60 w-full">
        <div class="flex flex-col">
            <div class="font-black text-3xl leading-180">News Updates</div>
            <div class="w-largetext text-base mt-10 leading-normal">
                Lorem ipsum dolor sit amet, adipiscing elit. Aenean commodo
                ligula eget dolor. Lorem ipsum dolor sit amet, consectetuer
                adipiscing elit. Aenean commodo ligula eget dolor. Lorem ipsum
                dolor sit amet, adipiscing elit.
            </div>
        </div>
        <div
            class="flex flex-row pt-28 pr-navbar"
            v-for="event in event"
            v-bind:key="event"
        >
            <div class="flex flex-col">
                <div v-if="event.types == 'upcoming'">
                    <LargeFeed>
                        event={{ event }} eventUpdates={{ eventUpdates }}
                    </LargeFeed>
                </div>
                <div v-if="event.types == 'past'">
                    <LargeFeed
                        >event={{ event }} eventUpdates={{
                            eventUpdates
                        }}</LargeFeed
                    >
                </div>
            </div>
            <div class="flex flex-col ml-10">
                <div class="flex flex-row">
                    <div v-if="event.types == 'app'">
                        <SmallFeed :event="event" />
                    </div>
                </div>
                <div v-if="event.types == 'past'">
                    <LargeFeed
                        >event={{ event }} eventUpdates={{
                            eventUpdates
                        }}</LargeFeed
                    >
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import LargeFeed from "@/components/news/LargeFeed.vue";
import SmallFeed from "@/components/news/SmallFeed.vue";
export default {
    name: "news",
    components: {
        LargeFeed,
        SmallFeed
    },
    data: function initData() {
        return {
            event: {},
            eventUpdates: {}
        };
    },
    mounted() {
        axios
            .get("http://0.0.0.0:8000/api/news/?format=json")
            .then(response => {
                let event = {};
                for (let i = 0; i < response.data.length; i++) {
                    event[response.data[i]["title"]] = response.data[i];
                }
                this.event = Object.assign({}, this.event, event);
            });
        axios
            .get("http://0.0.0.0:8000/api/news/updates/?format=json")
            .then(response => {
                let eventUpdates = {};
                for (let i = 0; i < response.data.length; i++) {
                    eventUpdates[response.data[i]["title"]] = response.data[i];
                }
                this.eventUpdates = Object.assign(
                    {},
                    this.eventUpdates,
                    eventUpdates
                );
            });
    }
};
</script>
