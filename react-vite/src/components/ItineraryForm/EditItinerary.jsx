import { useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { thunkItineraryById } from '../../redux/itinerary';
import ItineraryForm from './ItineraryForm';
import Loading from "../SubComponents/Loading";


const EditItinerary = () => {
    const dispatch = useDispatch();
    const { itineraryId } = useParams();
    const itinerary = useSelector((state) => state.itineraries.itineraryById?.[itineraryId]);

    useEffect(() => {
        if (itineraryId) {
        dispatch(thunkItineraryById(itineraryId)) 
        }
    }, [dispatch, itineraryId]);

    if (!itinerary) return <Loading />;

  return (
    Object.keys(itinerary).length > 1 && (
      <>
        <ItineraryForm
          itinerary={itinerary}
          formType="Update Your Itinerary"
        />
      </>
    )
  );
};

export default EditItinerary;