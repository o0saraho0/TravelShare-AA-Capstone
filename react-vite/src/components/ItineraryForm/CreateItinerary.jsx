import ItineraryForm from "./ItineraryForm";

const CreateItinerary = () => {
    const itinerary = {};
    return (
    <ItineraryForm
        itinerary={itinerary}
        formType="Create New Itinerary"
    />
    )
}

export default CreateItinerary;