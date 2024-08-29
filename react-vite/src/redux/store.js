import {
  legacy_createStore as createStore,
  applyMiddleware,
  compose,
  combineReducers,
} from "redux";
import thunk from "redux-thunk";
import sessionReducer from "./session";
import itineraryReducer from "./itinerary";
import activityReducer from "./activity";
import collectionReducer from "./collection";
import commentReducer from "./comment";
import imageReducer from "./image";

const rootReducer = combineReducers({
  session: sessionReducer,
  itineraries: itineraryReducer,
  activities: activityReducer,
  collections: collectionReducer,
  comments: commentReducer,
  images: imageReducer,
});

let enhancer;
if (import.meta.env.MODE === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = (await import("redux-logger")).default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
