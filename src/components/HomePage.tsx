import React from 'react';
import { Carousel } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './../index.css';

const Home: React.FC = () => {
  return (
    <Carousel>
      <Carousel.Item>
        <div
          className="d-flex align-items-center justify-content-center w-100"
          style={{
            height: '100vh',
            backgroundColor: '#94b492' // Brighter pastel green
          }}
        >
          <div className="text-center">
            <img 
              src="./../src/assets/foodbook-high-resolution-logo-transparent.png" // Assuming the logo is in the public directory
              style={{ width: '350px', marginBottom: '20px' }}
            />
          </div>
        </div>
      </Carousel.Item>

      <Carousel.Item>
        <div
          className="d-flex align-items-center justify-content-center w-100"
          style={{
            height: '100vh',
            backgroundColor: '#94b492' // Brighter pastel green
          }}
        >
          <div className="text-center">
            <h2 className="text">Discover, share, and enjoy delicious recipes from around the world!</h2>
            <button className="btn btn-custom">Explore more</button>
          </div>
        </div>
      </Carousel.Item>

      <Carousel.Item>
        <div
          className="d-flex align-items-center justify-content-center w-100"
          style={{
            height: '100vh',
            backgroundColor: '#94b492' // Brighter pastel green
          }}
        >
          <div className="text-center">
            <h2>Food Gallery</h2>
            <div className="d-flex justify-content-around">
              <img
                src="https://via.placeholder.com/150"
                alt="Food 1"
                className="img-thumbnail"
                style={{
                  backgroundColor: '#a8d5ba', // Brighter pastel green
                  borderColor: '#94b492'
                }}
              />
              <img
                src="https://via.placeholder.com/150"
                alt="Food 2"
                className="img-thumbnail"
                style={{
                  backgroundColor: '#a8d5ba', // Brighter pastel green
                  borderColor: '#94b492'
                }}
              />
              <img
                src="https://via.placeholder.com/150"
                alt="Food 3"
                className="img-thumbnail"
                style={{
                  backgroundColor: '#a8d5ba', // Brighter pastel green
                  borderColor: '#94b492'
                }}
              />
            </div>
          </div>
        </div>
      </Carousel.Item>
    </Carousel>
  );
};

export default Home;
