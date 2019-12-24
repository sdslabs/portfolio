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
            v-for="event_block in event"
            v-bind:key="event_block"
        >
            <div class="flex flex-col">
                <div v-if="event_block.event.types == 'upcoming'">
                    <LargeFeed
                        :event="event_block.event"
                        :eventUpdates="event_block.event_update"
                    />
                </div>
                <div v-if="event_block.event.types == 'online'">
                    <LargeFeed
                        :event="event_block.event" 
                        :eventUpdates="event_block.eventUpdates"
                    />
                </div>
            </div>
            <div class="flex flex-col ml-10">
                <div class="flex flex-row">
                    <div v-if="event_block.event.types == 'app'">
                        <SmallFeed :event="event_block.event" />
                    </div>
                </div>
                <div v-if="event_block.event.types == 'past'">
                    <LargeFeed
                        :event="event_block.event" 
                        :eventUpdates="event_block.eventUpdates"
                    />
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
            eventUpdates: []
        };
    },
    mounted() {
        axios
            .get("http://0.0.0.0:8000/api/news/?format=json")
            .then(response => {
                let events = response.data;
                let event = [];
                events.forEach(event_block => {
                    event.push(event_block);
                });
                this.event = Object.assign({}, this.event, event);
            });
    }
};
</script>
