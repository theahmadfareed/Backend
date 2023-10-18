import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import LandingPage from './Pages/LandingPage';
import SignUp from './Pages/SignUp';
import SignIn from './Pages/SignIn';
import CreateProject from './Pages/CreateProject';
import ProjectDetails from './Pages/ProjectDetails';
import Comparison from './Pages/Comparison';
import Dashboard from './Pages/Dashboard';
import Reports from './Pages/Reports';
import ContactUs from './Pages/ContactUs';
import Navbar from './Components/Navbar/Navbar';

function App() {
  return (
    <div >
      <BrowserRouter>
        <Navbar/>
        <Routes>
          <Route path='/' element={<LandingPage />} />
          <Route path='/sign-up' element={<SignUp />} />
          <Route path='/sign-in' element={<SignIn />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/create-project' element={<CreateProject />} />
          <Route path='/project-details/:projectId' element={<ProjectDetails />} />
          <Route path='/comparison' element={<Comparison />} />
          <Route path='/reports' element={<Reports />} />
          <Route path='/contact-us' element={<ContactUs />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
