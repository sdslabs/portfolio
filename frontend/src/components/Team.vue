<template>
  <div class="flex flex-col-reverse pt-60 md:flex-row md:pt-60 md:w-full md:justify-center">
    <div class="flex flex-row ml-8 mr-8 md:mr-26">
        <div class="flex flex-col w-96 h-80 bg-team mt-36">
            <div class="self-center"><img class="w-64 mt-12" src="@/assets/images/dev.svg"/></div>
            <div class="self-center mt-8">
                <span class="font-black text-3xl md:text-4xl">20 </span>
                <span class="font-black text-lg md:text-xl">Developers</span>
            </div>
        </div>
        <div class="flex flex-col w-64 h-80 bg-team ml-16 md:ml-20">
            <div class="self-center"><img class="w-28 mt-20" src="@/assets/images/des.svg"/></div>
            <div class="self-center mt-1">
                <span class="font-black text-3xl md:text-4xl">9 </span>
                <span class="font-black text-lg md:text-xl">Designers</span>
            </div>
        </div>
        <div class="w-96 h-48 bg-team mt-96 -ml-56 md:-ml-64 ">
            <div class="self-center text-center mt-16">
                <span class="font-black text-3xl md:text-4xl">40+ </span>
                <span class="font-black text-lg md:text-xl">Alumni</span>
            </div>
        </div>
    </div>
    <div class="flex flex-col w-auto ml-6 mr-6 md:ml-26">
        <div class="font-black text-3xl leading-loose md:w-88">Our Team</div>
        <div class="md:w-144 md:mt-14 mt-10 font-semibold text-base leading-normal">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl.</div>
        <div><Button class="mt-14" v-bind:native=true url="https://team.sdslabs.co/" text="Open Teampage"/></div>
    </div>
  </div>
</template>

<script>
import Button from "@/components/Button.vue"
export default {
    name: "team",
    components: {
        Button
    }
}
</script>
