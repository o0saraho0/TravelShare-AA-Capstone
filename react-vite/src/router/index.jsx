import { createBrowserRouter } from "react-router-dom";
import Layout from "./Layout";
import LandingPage from "../components/LandingPage/LandingPage";
import ItinerariesList from "../components/ItinerariesListPage";
import ItineraryDetail from "../components/ItineraryDetailPage";
import ItinerariesManage from "../components/ItinerariesManage/ItinerariesManage";
import UserProfile from "../components/UserProfile/UserProfile";
import ItinerariesByCategory from "../components/ItinerariesByCategory/ItinerariesByCategory";
import CreateItinerary from "../components/ItineraryForm/CreateItinerary";
import EditItinerary from "../components/ItineraryForm/EditItinerary";
import ActivitiesForm from "../components/ActivitiesForm";
import CollectionsManage from "../components/CollectionManage";
import NotFoundPage from "../components/SubComponents/NotFound";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <LandingPage />,
      },
      {
        path: "/itineraries",
        element: <ItinerariesList />,
      },
      {
        path: "/itineraries/category/:categoryId",
        element: <ItinerariesByCategory />,
      },
      {
        path: "/itineraries/:itineraryId",
        element: <ItineraryDetail />,
      },
      {
        path: "/itineraries/current",
        element: <ItinerariesManage />,
      },
      {
        path: "/itineraries/traveler/:travelerId",
        element: <UserProfile />,
      },
      {
        path: "/itineraries/new",
        element: <CreateItinerary />,
      },
      {
        path: "/itineraries/:itineraryId/edit",
        element: <EditItinerary />,
      },
      {
        path: "/itineraries/:itineraryId/activities",
        element: <ActivitiesForm />,
      },
      {
        path: "/collections/current",
        element: <CollectionsManage />,
      },
      {
        path: "*",
        element: <NotFoundPage />,
      },
    ],
  },
]);
