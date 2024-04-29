import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  Link
} from "react-router-dom"

import Layout from './components/Layout';
import Home from './pages/home';
import QueryGenerator from './pages/QueryGenerator';
import CodeGenerator from './pages/CodeGenerator';
import NotFound from './pages/NotFound';
import utilsContext from "./context/utilsContext";

import Playground from './pages/Playground';
import Ace from './pages/Ace';
const router = createBrowserRouter(createRoutesFromElements(
  <Route path="/" element={<Layout />}>
    <Route index element={<Home/>} />
    {/* <Route path='/chatPg' element={<ChatPg/>}/> */}
    <Route path='/query-generator' element={<QueryGenerator/>}/>
    <Route path='/code-generator' element={<CodeGenerator />} />
    <Route path='/pg' element={<Playground/>}/>
    <Route path='/ace' element={<Ace/>}/>
    <Route path="*" element={<NotFound />} />
  </Route>
))

export default function App() {
  let [sidebarData, setSidebarData] = React.useState(null);
  let [mainContentInput, setMainContentInput] = React.useState("");
  let [queryResponse, setQueryResponse] = React.useState(null);

  return (
    <utilsContext.Provider value={[sidebarData, setSidebarData, mainContentInput, setMainContentInput, queryResponse, setQueryResponse]}>
        <RouterProvider router={router} />
    </utilsContext.Provider>
  )
}