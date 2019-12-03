<template>
  <div class="flex flex-row pt-60 w-full justify-center">
    <div class="flex flex-row mr-26">
        <div class="flex flex-col w-96 h-80 bg-team mt-36">
            <div class="self-center"><img class="w-64 mt-12" src="@/assets/images/dev.svg"/></div>
            <div class="self-center mt-8">
                <span class="font-black text-4xl">20 </span>
                <span class="font-black text-xl">Developers</span>
            </div>
        </div>
        <div class="flex flex-col w-64 h-80 bg-team ml-20">
            <div class="self-center"><img class="w-28 mt-20" src="@/assets/images/des.svg"/></div>
            <div class="self-center mt-1">
                <span class="font-black text-4xl">9 </span>
                <span class="font-black text-xl">Designers</span>
            </div>
        </div>
        <div class="w-96 h-48 bg-team mt-96 -ml-64">
            <div class="self-center text-center mt-16">
                <span class="font-black text-4xl">40+ </span>
                <span class="font-black text-xl">Alumni</span>
            </div>
        </div>
    </div>
    <div class="flex flex-col ml-26">
        <div class="font-black text-3xl leading-loose w-88">Our Team</div>
        <div class="w-144 mt-14 font-semibold text-base leading-normal">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl.</div>
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
