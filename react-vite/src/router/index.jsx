import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import LandingPage from '../components/LandingPage/LandingPage';
import ItinerariesList from '../components/ItinerariesListPage';
import ItineraryDetail from '../components/ItineraryDetailPage'
import ItineraryForm from '../components/ItineraryForm';

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
        path: "/itineraries/new",
        element: <ItineraryForm />
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