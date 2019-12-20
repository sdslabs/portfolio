<template>
    <div class="flex flex-col pt-60 pl-60 w-full">
        <div class="flex flex-col">
            <div class="font-black text-3xl leading-180">News Updates</div>
            <div class="w-largetext text-base mt-10 leading-normal">Lorem ipsum dolor sit amet, adipiscing elit. Aenean commodo ligula eget dolor. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Lorem ipsum dolor sit amet, adipiscing elit.</div>
        </div>
        <div class="flex flex-row pt-28 pr-navbar" v-for="event in event" v-bind:key="event" >
            <div class="flex flex-col">
                <div v-if="event.types =='upcoming'">
                    <div class="w-feed h-auto shadow-feed pl-10 pt-10 pr-navbar">
                        <Label text="UPCOMING EVENT"/>
                        <div class="flex flex-col h-72 mt-12 pb-12">
                            <div class="font-extrabold text-xl leading-180">{{ event.title }}</div>
                            <div class="mt-8 text-base font-semibold leading-170">{{ event.timing }}</div>
                            <div class="mt-16 text-base leading-normal">{{ event.description }}</div>
                        </div>
                        <div class="flex flex-col mt-12 pb-10" v-for="(eventUpdates, index) in eventUpdates" v-bind:key="eventUpdates">
                            <div class="font-semibold text-base leading-170">{{ index+1 }} Updates</div>
                            <UpdateCard>
                                title= {{ eventUpdates.title }}
                                description= {{ eventUpdate.description }}
                            </UpdateCard>
                        </div>
                        <div class="mt-10 font-extrabold text-base text-red mb-8 leading-170">Know more</div>
                    </div>
                </div>
                <div v-if="event.types == 'past'">
                    <div class="mt-10 w-feed h-auto shadow-feed pl-10 pt-10 pr-navbar mb-64">
                        <Label text="PAST EVENT"/>
                        <div class="flex flex-col pb-14">
                            <div class="mt-14 font-extrabold text-xl leading-180">{{ event.title }}</div>
                            <div class="mt-8 font-semibold text-base leading-170">{{ event.timing }}</div>
                            <div class="mt-14 text-base leading-normal">{{ event.description }}</div>
                        </div>
                        <div class="mt-10 font-extrabold text-base text-green mb-8 leading-170">Know more</div>
                    </div>
                </div>
            </div>
            <div class="flex flex-col ml-10">
                <div class="flex flex-row">
                    <div v-if="event.types == 'app'">
                        <div class="w-event h-auto shadow-feed pl-10 pt-10 pr-10">
                            <Label text="APP UPDATE"/>
                            <div class="flex flex-col mt-10 pb-10">
                                <div class="font-extrabold text-xl leading-180">{{ event.title }}</div>
                                <div class="mt-20 text-base leading-normal">{{ event.description }}</div>
                            </div>
                            <div class="mt-8 font-extrabold text-base text-blue mb-8 leading-170">Check Now</div>
                        </div>
                        <div class="w-event h-auto shadow-feed pl-10 pt-10 pr-10 ml-10">
                            <Label text="ONLINE COMPETITION"/>
                            <div class="flex flex-col mt-10 pb-10">
                                <div class="font-extrabold text-xl leading-180">{{ event.title }}</div>
                                <div class="mt-6 font-semibold text-base leading-170">{{ event.timing }}</div>
                                <div class="mt-14 text-base leading-normal">{{ event.description }}</div>
                            </div>
                            <div class="mt-8 font-extrabold text-base text-yellow mb-8 leading-170">Check Now</div>
                        </div>
                    </div>
                </div>
                <div v-if="event.types == 'past'">
                    <div class="mt-10 w-feed h-auto shadow-feed pl-10 pt-10 pr-navbar mb-64">
                        <Label text="PAST EVENT"/>
                        <div class="flex flex-col pb-14">
                            <div class="mt-14 font-extrabold text-xl leading-180">{{ event.title }}</div>
                            <div class="mt-8 font-semibold text-base leading-170">{{ event.timing}}</div>
                            <div class="mt-14 text-base leading-normal">{{ event.description }}</div>
                        </div>
                        <div class="flex flex-col pb-12 mt-14">
                            <div class="font-semibold text-base leading-normal">1 Update</div>
                            <div class="mt-8 font-extrabold text-base leading-180">POST WORKSHOP PHOTOS</div>
                        </div>
                        <div class="mt-10 font-extrabold text-base text-purple mb-8 leading-180">Know more</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Label from "@/components/Label.vue";
import UpdateCard from "@/components/news/UpdateCard.vue";
export default {
    name: "news",
    components: {
        Label,
        UpdateCard
    },
    data: function initData() {
        return {
            event: {},
            appUpdate: {},
            onlineCompetition: {},
            eventUpdates: {}
        }
    },
    mounted() {
        axios
            .get('http://0.0.0.0:8000/api/news/?format=json')
            .then(response => {
                let event = {}
                for(let i = 0; i < response.data.length; i++) {
                    event[response.data[i]["title"]] = response.data[i]
                }
                this.event = Object.assign({}, this.event, event);
            })
        axios
            .get('http://0.0.0.0:8000/api/news/updates/?format=json')
            .then(response => {
                let eventUpdates = {}
                for(let i = 0; i < response.data.length; i++) {
                    eventUpdates[response.data[i]["title"]] = response.data[i]
                }
                this.eventUpdates = Object.assign({}, this.eventUpdates, eventUpdates);
            })
    },
};
</script>
