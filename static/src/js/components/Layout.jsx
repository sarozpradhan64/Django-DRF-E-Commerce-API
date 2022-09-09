import { InertiaLink } from "@inertiajs/inertia-react";
import {Link} from '@inertiajs/inertia-react';

const Layout = ({children}) => (
  <>
<div className="min-h-full">
  <h1>Saroj Pradhan</h1>
  <Link href="/login">Admin login</Link>
  <div className="py-10">
    <main>
      <div className="max-w-7xl mx-auto sm:px-6 lg:px-8">
        
        <div className="px-4 py-8 sm:px-0">
          <div className="bg-white rounded-lg h-96 p-3">
            {children}
          </div>
        </div>
       
      </div>
    </main>
  </div>
</div>

  </>
)



export default page => <Layout>{page}</Layout>;