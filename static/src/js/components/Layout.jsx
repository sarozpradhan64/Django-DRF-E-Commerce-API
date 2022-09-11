import { InertiaLink } from "@inertiajs/inertia-react";
import {Link} from '@inertiajs/inertia-react';

const Layout = ({children}) => (
  <>
<div className="min-h-full">
            {children}
          </div>
  </>
)



export default page => <Layout>{page}</Layout>;