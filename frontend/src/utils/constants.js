const getBaseURL = () => {
    const hostname = window.location.hostname;
    if (hostname.endsWith(".co.in")) {
        return "https://portfolio-backend.sdslabs.co.in";
    } else {
        return "https://portfolio-backend.sdslabs.co";
    }
};

export const CONFIG = {
    baseURL: getBaseURL(),
    colors: ["blue", "red", "green", "yellow", "purple", "orange"],
    mobileSize: 576,
};
