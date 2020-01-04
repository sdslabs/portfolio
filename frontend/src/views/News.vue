<template>
    <div
        :key="key"
        class="flex flex-col ml-10 mr-10 sm:ml-0 sm:mr-0 pt-44 sm:pt-60 sm:pl-60 sm:w-full"
    >
        <div class="flex flex-col">
            <div class="font-black text-3xl leading-180">News Updates</div>
            <div class="sm:w-largetext sm:text-base mt-10 sm:leading-normal text-lg text-grey leading-170">
                Lorem ipsum dolor sit amet, adipiscing elit. Aenean commodo
                ligula eget dolor. Lorem ipsum dolor sit amet, consectetuer
                adipiscing elit. Aenean commodo ligula eget dolor. Lorem ipsum
                dolor sit amet, adipiscing elit.
            </div>
        </div>
        <div id="grid" class="sm:grid sm:w-news pt-24 pb-24">
            <div
                id="grid-item"
                class="sm:grid-item sm:pr-navbar sm:w-event"
                v-for="event_block in event"
                v-bind:key="event_block.event.title"
            >
                <div>
                    <div
                    id="feed"
                    class="mb-10 sm:w-feed"
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
                        <SmallFeed class="mb-10 sm:w-event" :event="event_block.event" />
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
                    class="mb-10 sm:w-event"
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
                class="mb-10 sm:w-event"
                    v-if="
                        event_block.event.types == 'app update' &&
                            event_block.event.priority == 'small'
                    "
                >
                    <SmallFeed :event="event_block.event" />
                </div>
                <div class="mb-10 sm:w-feed" v-if="event_block.event.types == 'past event' && event_block.event.priority == 'large'">
                    <LargeFeed
                        :event="event_block.event"
                        :eventUpdates="event_block.event_update"
                    />
                </div>
                 <div class="mb-10 sm:w-feed" v-if="event_block.event.types == 'past event' && event_block.event.priority == 'small'">
                    <SmallFeed :event="event_block.event"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
// import Masonry from "masonry-layout";
import LargeFeed from "@/components/news/LargeFeed.vue";
import SmallFeed from "@/components/news/SmallFeed.vue";
import { CONFIG } from "@/utils/constants.js";
export default {
    name: "news",
    components: {
        LargeFeed,
        SmallFeed
    },
    data: function initData() {
        return {
            event: {},
            eventUpdates: [],
            key: 0
        };
    },
    methods: {
        windowResize() {
            var elem = document.getElementsByClassName("sm:grid")[0];
            if (window.innerWidth < 576) {
                elem.id = "";
                this.key = 1;
            } else {
                elem.id = "grid";
                this.key = 2;
            }
        },
        masonry() {
            var elem = document.getElementById("grid");
            var msnry = new Masonry(elem, {
                // options
                itemSelector: "#grid-item",
                columnWidth: "#feed",
                gutter: 24,
                percentPosition: true
            });
        }
    },
    created() {
        window.addEventListener("resize", this.windowResize);
    },
    async mounted() {
        await axios
            .get(CONFIG.NewsPageURL)
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
        if (window.innerWidth < 576) {
            var elem = document.getElementById("grid");
            elem.id = "";
        }
        this.masonry();
    },
    updated() {
        if (window.innerWidth > 576) {
            this.masonry();
        }
    },
    destroyed() {
        window.removeEventListener("resize", this.windowResize);
    }
};
</script>
