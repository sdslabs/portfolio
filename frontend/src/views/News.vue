<template>
    <div
        class="flex flex-col ml-10 mr-10 md:ml-0 md:mr-0 pt-44 md:pt-60 md:pl-60 md:w-full"
    >
        <div class="flex flex-col">
            <div class="font-black text-3xl leading-180">News Updates</div>
            <div class="md:w-largetext text-base mt-10 leading-normal">
                Lorem ipsum dolor sit amet, adipiscing elit. Aenean commodo
                ligula eget dolor. Lorem ipsum dolor sit amet, consectetuer
                adipiscing elit. Aenean commodo ligula eget dolor. Lorem ipsum
                dolor sit amet, adipiscing elit.
            </div>
        </div>
        <div class="pt-24 pb-24 md:grid">
            <div
                class="md:pr-navbar md:w-event"
                v-for="event_block in event"
                v-bind:key="event_block"
            >
                <div>
                    <div
                    class="md:grid-item mb-10 md:w-feed"
                        v-if="
                            event_block.event.types == 'upcoming event' &&
                                event_block.event.priority == 'large'
                        "
                    >
                        <LargeFeed
                            :event="event_block.event"
                            :eventUpdates="event_block.event_update"
                        />
                    </div>
                    <div
                        v-if="
                            event_block.event.types == 'upcoming event' &&
                                event_block.event.priority == 'small'
                        "
                    >
                        <SmallFeed class="md:grid-item mb-10 md:w-event" :event="event_block.event" />
                    </div>
                    <div
                        v-if="
                            event_block.event.types == 'online competition' &&
                                event_block.event.priority == 'large'
                        "
                    >
                        <LargeFeed
                            :event="event_block.event"
                            :eventUpdates="event_block.event_update"
                        />
                    </div>
                    <div
                    class="md:grid-item mb-10 md:w-event"
                        v-if="
                            event_block.event.types == 'online competition' &&
                                event_block.event.priority == 'small'
                        "
                    >
                        <SmallFeed :event="event_block.event" />
                    </div>
                </div>
                <div
                    v-if="
                        event_block.event.types == 'app update' &&
                            event_block.event.priority == 'large'
                    "
                >
                    <LargeFeed
                        :event="event_block.event"
                        :eventUpdates="event_block.event_update"
                    />
                </div>
                <div
                class="md:grid-item mb-10 md:w-event"
                    v-if="
                        event_block.event.types == 'app update' &&
                            event_block.event.priority == 'small'
                    "
                >
                    <SmallFeed :event="event_block.event" />
                </div>
                <div class="md:grid-item mb-10 md:w-feed" v-if="event_block.event.types == 'past event'">
                    <LargeFeed
                        :event="event_block.event"
                        :eventUpdates="event_block.event_update"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script type="text/javascript" src="masonry.pkgd.js">
</script>
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
                let eventList = [];
                let event = [];
                events.forEach(event_block => {
                    eventList.push(event_block);
                });
                eventList.forEach(events_list => {
                    if (events_list.event.types === "upcoming event")
                        event.push(events_list);
                });
                eventList.forEach(events_list => {
                    if (events_list.event.types === "app update")
                        event.push(events_list);
                });
                eventList.forEach(events_list => {
                    if (events_list.event.types === "online competition")
                        event.push(events_list);
                });
                eventList.forEach(events_list => {
                    if (events_list.event.types === "past event")
                        event.push(events_list);
                });
                this.event = Object.assign({}, this.event, event);
            });
        var elem = document.querySelector(".grid");
        var msnry = new Masonry(elem, {
            itemSelector: ".grid-item",
            columnWidth: 1200,
        });
    }
};
</script>
