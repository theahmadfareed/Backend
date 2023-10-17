import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import LandingPage from './Pages/LandingPage';
import SignUp from './Pages/SignUp';
import SignIn from './Pages/SignIn';
import CreateProject from './Pages/CreateProject';
import ProjectDetails from './Pages/ProjectDetails';
import Dashboard from './Pages/Dashboard';

function App() {
  return (
    <div >
      <BrowserRouter>
      <Routes>
        <Route path='/' element={<LandingPage />} />
        <Route path='/sign-up' element={<SignUp />} />
        <Route path='/sign-in' element={<SignIn />} />
        <Route path='/create-project' element={<CreateProject />} />
        <Route path='/dashboard' element={<Dashboard />} />
        <Route path='/project-details/:projectId' element={<ProjectDetails />} />
      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
