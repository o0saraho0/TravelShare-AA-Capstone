import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import LandingPage from '../components/LandingPage/LandingPage';
import ItinerariesList from '../components/ItinerariesListPage';
import ItineraryDetail from '../components/ItineraryDetailPage'
import ItinerariesManage from '../components/ItinerariesManage/ItinerariesManage';
import CreateItinerary from '../components/ItineraryForm/CreateItinerary'
import EditItinerary from '../components/ItineraryForm/EditItinerary';
import ActivitiesForm from '../components/ActivitiesForm'


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
        element: <ItinerariesList />
      },
      {
        path: "/itineraries/:itineraryId",
        element: <ItineraryDetail />
      },
      {
        path: "/itineraries/current",
        element: <ItinerariesManage />
      },
      {
        path: "/itineraries/new",
        element: <CreateItinerary />
      },
      {
        path: "/itineraries/:itineraryId/edit",
        element: <EditItinerary />
      },
      {
        path: "/itineraries/:itineraryId/activities",
        element: <ActivitiesForm />
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
    ],
  },
]);